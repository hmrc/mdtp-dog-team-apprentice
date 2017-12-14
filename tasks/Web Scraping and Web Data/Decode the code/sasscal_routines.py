from lxml import html
import requests
import numpy as np
import datetime as dt
import pandas as pd
import pickle

url_base='http://www.sasscalweathernet.org/weatherstat_hourly_we.php?loggerid_crit='
months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

def getFrame(ID):
    url = "%s%d"%(url_base,ID)
    print url
    page = requests.get(url)
    tree = html.fromstring(page.content)
    tmp = tree.xpath("//select[@name='date_crit']/option/text()")
    nt = len(tmp)
    times = np.zeros(nt,dtype=object)
    for i,t in enumerate(tmp):
        t2 = t.split(' ')
        times[i] = dt.datetime(int(t2[2]),months[t2[1]],int(t2[0]))
    ncol = len(tree.xpath("//tr[@bgcolor='#344974']")[0].getchildren())
    tmp = tree.xpath('//td[@id="weather_data"]')[:2*ncol]
    header = np.zeros(ncol,dtype=object)
    units = {}# np.zeros(15,dtype=object)
    for i in range(ncol):
        header[i] = (tmp[i].text_content()).strip('.').strip('u')
        units[header[i]] =  stripWeird(tmp[i+ncol].text_content())
    return times[::-1], header, units

def getList():
    url = 'http://www.sasscalweathernet.org/index.php?MIsoCode=00'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    a = [xx.attrib['href'] for xx in x if 'href' in xx.items()[0]]
#    names=tree.xpath('//a[@class="qmparent"]/text()')[1:-4]
#    a = [xx.attrib['href'] for xx in names if 'href' in xx.items()[0]]
    return tree

def stripWeird(name):
    out = ''
    for char in name:
        if ord(char) < 127:
            out+=char
    return out
    

def getDay(ID,t,n):
        print t
        url = "%s%s&date_crit_daily=%d-%02d-%02d"%(url_base,ID,t.year,t.month,t.day)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        x=tree.xpath('//td[@id="weather_data"]/text()')
        nt = len(x[n+2:])/(n-1)
        out = np.zeros((nt,n),dtype=object)
        
        out[:,1:]=np.array(x[n+2:]).reshape((nt,n-1))
        for tt in range(nt):
            for y in range(n-2):
                try:
                    out[tt,y+2] = float(out[tt,y+2])
                except:
                    out[tt,y+2] = np.nan
        for i,tt in enumerate(out[:,1]):
            tmp = tt.split(':')
            if len(tmp)>1:
                   out[i,1] = int(tmp[0])+int(tmp[1])/60.0
        out[:,0] = [t+dt.timedelta(float(i)/24.0) for i in out[:,1]]
        return out

def makeDataFrame(times,header,units,data):
    tmp = {}
    for i,name in enumerate(header[1:]):
        tmp[name] = data[:,i+1]
    df = pd.DataFrame(data=tmp,index=data[:,0],dtype=float)
    df = df[header[1:]]
    return df

def metadata(ID):
    url = "http://www.sasscalweathernet.org/weatherstat_infosheet_we.php?loggerid_crit=%d"%ID
    page = requests.get(url)
    tree = html.fromstring(page.content)
    tmp=tree.xpath("//table[@id='borderlinie_dott']//td[@id='publfont']/text()")
    indices = [0,2,4,6,11,13,15]
    meta= {}
    meta['sensors']= {}
    meta['heights']= {}
    for i in indices:
        meta[tmp[i].strip('\r\n').strip(':')] = tmp[i+1].strip('\r\n')

    indices = [17,21,25,29,32,35,39,43]

    names=['Leaf Wetness','Ground Temperature','Rain','Barometric Pressure','Data Logger','Radiation','Temperatur/Humidity','Wind']
    indices =[]# = [tmp.index(n) for n in names]
    for n in names:
        try:
            indices.append(tmp.index(n))
        except ValueError:
            continue
           
    
    for i in indices:
        meta['sensors'][tmp[i].strip('\r\n').strip(':')] = tmp[i+1].strip('\r\n')
        meta['heights'][tmp[i].strip('\r\n').strip(':')] = tmp[i+2].strip('\r\n')

    for i in range(len(meta['Altitude'])):
        try:
            meta['Altitude'] = int(meta['Altitude'][:-i])
            break
        except ValueError:
            continue
    return meta

def assign_meta(meta,header):
    sensors = {}
    heights = {}

    convert = {'LeafWetness':'Leaf Wetness','SurfaceTemp':'Ground Temperature','Precip':'Rain',\
        'Barom.Press':'Barometric Pressure','BatteryVoltage':'Data Logger','SolarIrradiance':'Radiation',\
        'AirTemp':'Temperatur/Humidity', 'Humidity':'Temperatur/Humidity'}

    for name in header:
        if 'Wind' in name:
            convert[name] = 'Wind'
        if name in convert.keys():
            sensors[name] = meta['sensors'][convert[name]]
            heights[name] = meta['heights'][convert[name]]
    sensors['Hour'],heights['Hour'] = '', ''
    meta['sensors'] = sensors
    meta['heights'] = heights
    return meta

def writeDataCSV(df,meta,filename):
    outfile = open(filename,'w')
    for name in meta.keys():
        if type(meta[name]) != dict:
            outfile.write("%s,%s \n"%(name,meta[name]))
    outfile.write(',')
    for name in df.keys():
        outfile.write('%s,'%(meta['sensors'][name]))
    outfile.write('\n,')
    for name in df.keys():
        outfile.write('%s,'%(meta['heights'][name]))
    outfile.write('\n')
    outfile.close()
    df.to_csv(filename,mode='a')    

def writeDataPKL(df,meta,filename):
    pickle.dump((df,meta),file(filename,'w'))

def download_sasscal(ID):
    times,header,units=getFrame(ID)
    meta = metadata(ID)
#    times = times[:3]
    meta['units'] = units
    meta = assign_meta(meta,header)
    for i,t in enumerate(times):
        if i==0:
            data = getDay(ID,t,len(header))
        else:
            data = np.concatenate((data,getDay(ID,t,len(header))),axis=0)
    df = makeDataFrame(times,header,units,data)
    writeDataPKL(df,meta,'%d.pkl'%ID)
    return df,meta

def read_sasscal(ID):
    filename='%d.pkl'%ID
    df,meta = pickle.load(file(filename,'r'))
    return df,meta

"""
url='http://www.sasscalweathernet.org/weatherstat_hourly_we.php?loggerid_crit=31203'
     http://www.sasscalweathernet.org/weatherstat_hourly_we.php?loggerid_crit=31203&date_crit_daily=2010-10-07
url='http://www.sasscalweathernet.org/weatherstat_hourly_we.php?loggerid_crit=31203&date_crit_daily='#2017-09-01'

t0 = dt.datetime(2013,01,01)
t1 = dt.datetime(2013,01,02)

nt = (t1-t0).days




data = np.zeros((nt*24,17),dtype=object)
#tree.xpath("//select[@name='date_crit']/option/text()")[-1]
t=t0
url1='http://www.sasscalweathernet.org/weatherstat_hourly_we.php?loggerid_crit=31203&date_crit_daily='#2017-09-01'

for i in range(nt):
    print t
    url = "%s%d-%02d-%02d"%(url1,t.year,t.month,t.day)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    x=tree.xpath('//td[@id="weather_data"]/text()')
    data[24*i:24*(i+1),3:]=np.array(x[17:]).reshape((24,14))
    data[24*i:24*(i+1),0] = t.year
    data[24*i:24*(i+1),1] = t.month
    data[24*i:24*(i+1),2] = t.day
    t = t+dt.timedelta(1)

outfile = file('out2.csv','w')

for i in range(nt*24):
    for j in range(17):
        try:
            outfile.write("%f,"%(float(data[i,j])))
        except ValueError:
            outfile.write(",")
    outfile.write("\n")
outfile.close()
"""
