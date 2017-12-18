from __future__ import division
from pylab import *
import os.path

def readFile():
    exist = False
    while not exist:
        fname = raw_input("Enter the file name: ")
        if not os.path.exists(fname):
            print ("The file called",fname,"does not exist. Please try again.")
        else:
            exist = True
    ctr=0
    fulltext=[]

    f = open(fname,'r')
    for line in f:
        line=line.lower()
        for ch in line:
            if ch>='a' and ch<='z':
                fulltext.append(ch)
    text = array(fulltext)
    return text



def readKey():
    count = zeros(26)
    done = False
    while not done:
        key = readFile()
        if size(key) != 26:
            print ("The key must have 26 letters! Try again.")
        else:
            done = True
        for i in arange(0,26):
            count[i]=0
        for i in arange(0,26):
            c = ord(key[i])-ord('a')
        count[c] = count[c] + 1
        if count[c]>1:
            print ("Each letter must occur EXACTLY once in the key! Try again.")
            done = False
            i = 26
    return key


def readString():
    Str = raw_input("Enter the string: ")
    Str=Str.lower()
    return Str


def stringHere(text, pos, sub):
    i=0
    same=True
    if pos+len(sub) > len(text):
      same = False;
    else:
        while i<len(sub):
            if text[pos+i] != sub[i]:
                same = False
            i=i+1
        return same


def IntArrayToText(numberArray):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    #matches each number 0-25 to a letter
    toChar = dict([(i , alpha[i]) for i in range(len(alpha))])
    #attaches a number to each letter
    chars = list(map(lambda i: toChar[i], numberArray))
    text = ''.join(chars)
    return text



def TextToIntArray(text):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    #matches each letter to a number 0-25
    toInt = dict([(alpha[i], i) for i in range(len(alpha))])
    #map doesn't work in python3 - hence list - attaches letter to each number
    textInts = list(map(lambda c: toInt[c], text))
    intArray = array(textInts)
    return intArray

