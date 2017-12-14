import matplotlib.pyplot as plt
from lxml import html
import requests
import numpy as np
import datetime as dt
import pandas as pd
import pickle

from sasscal_routines import *

ID = 108
df,meta = download_sasscal(ID)

#df,meta = read_sasscal(ID)
