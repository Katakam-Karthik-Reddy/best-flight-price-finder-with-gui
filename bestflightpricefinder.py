import os
import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import *

from airportCodes import loadAirports, getAirportCode
from easymytrip import getEasyMyTripFlights
from cleartrip import getClearTripFlights
from makemytrip import getMakeMyTripFlights
from ixigo import getIxigoflights



fromplace = 'bangalore'
toplace = 'delhi'

flights1 =[]
T1 = Thread(target= getEasyMyTripFlights, args=(fromplace, toplace, flights1,))
T1.start()
T1.join()

flights2 = []
T2 = Thread(target=getClearTripFlights, args=(fromplace, toplace, flights2,))
T2.start()
T2.join()

flights3 = []
T3 = Thread(target =getMakeMyTripFlights, args=(fromplace, toplace, flights3))
T3.start()
T3.join()

flights4 = []
T4 = Thread(target= getIxigoflights, args =(fromplace, toplace, flights4))
T4.start()
T4.join()

print("easymytrip")
for f in flights1:
    print(f)
print("cleartrip")
for f in flights2:
    print(f)

print("makemytrip")
for f in flights3:
    print(f)

print("ixigotrip")
for f in flights4:
    print(f)

flightname = []
starttime = []
endtime = []
totaljourneytime = []
totalstops = []
price = []


for f in flights1:
    flightname.append(f.flightname)
    starttime.append(f.starttime)
    endtime.append(f.endtime)
    totaljourneytime.append(f.totaljourneytime)
    totalstops.append(f.totalstops)
    price.append(f.price)


for f in flights2:
    flightname.append(f.flightname)
    starttime.append(f.starttime)
    endtime.append(f.endtime)
    totaljourneytime.append(f.totaljourneytime)
    totalstops.append(f.totalstops)
    price.append(f.price)


for f in flights3:
    flightname.append(f.flightname)
    starttime.append(f.starttime)
    endtime.append(f.endtime)
    totaljourneytime.append(f.totaljourneytime)
    totalstops.append(f.totalstops)
    price.append(f.price)



for f in flights4:
    flightname.append(f.flightname)
    starttime.append(f.starttime)
    endtime.append(f.endtime)
    totaljourneytime.append(f.totaljourneytime)
    totalstops.append(f.totalstops)
    price.append(f.price)


dic = {"flightname": flightname, "starttime": starttime, "endtime": endtime, "totaltourneytime": totaljourneytime, "totalstop": totalstops, "price": price }
dt = pd.DataFrame(dic)
print(dt)
filename = 'flightdata.csv'
cur_path = 'D:\rpa'
p = os.path.dirname(cur_path)
path = os.path.join(p, filename)
dt.to_csv(path)

