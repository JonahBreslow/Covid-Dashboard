
# coding: utf-8



import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import urllib
import datetime as dt
import pytz


base_url = 'https://covid19.mathdro.id/api/countries/US'
sauce = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(sauce, 'html.parser')
kpiValueString = str(soup)
print(kpiValueString)


Confirmed_str = str(re.findall('confirmed":{"value":\d+', kpiValueString))
Confirmed_num = int(re.findall('\d+', Confirmed_str)[0])
print(Confirmed_num)


Recovered_str = str(re.findall('recovered":{"value":\d+', kpiValueString))
Recovered_num = int(re.findall('\d+', Recovered_str)[0])
print(Recovered_num)


Deaths_str = str(re.findall('deaths":{"value":\d+', kpiValueString))
Deaths_num = int(re.findall('\d+', Deaths_str)[0])
print(Deaths_num)


import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('kpi-scraper-04e9ab4a1bf9.json', scope)
# credentials = '<oauth2client.service_account.ServiceAccountCredentials at 0x2024ab540f0>'

# credentials
gc = gspread.authorize(credentials)

wks = gc.open('KPI_Data').sheet1
#timestamp_wks = gc.open('KPI_Data').Sheet1

# print(wks.get_all_records())

# wks.update_acell('A1', 'KPI')




new_timezone = pytz.timezone("US/Pacific")
now = dt.datetime.now(new_timezone)

if (int(now.strftime("%d"))<10):
    day = now.strftime("%d")[1]
else:
    day = now.strftime("%d")[0]+" "+now.strftime("%d")[1]



if (int(now.strftime("%m"))<10):
    month = now.strftime("%m")[1]
else:
    month = now.strftime("%m")[0]+" "+now.strftime("%m")[1]


minute = now.strftime("%M")[0]+" 0"


year = now.strftime("%Y")[0]+' '+now.strftime("%Y")[1]+' '+now.strftime("%Y")[2]+' '+ now.strftime("%Y")[3]
hour = str(int(now.strftime("%I")))
AMPM = now.strftime("%p")[0]+" "+now.strftime("%p")[1]

timestamp = month+" / "+day+" / "+year+"   "+hour+" : "+minute+"   "+AMPM
print(timestamp)


wks.update_acell('B2', Confirmed_num)
wks.update_acell('B3', Recovered_num)
wks.update_acell('B4', Deaths_num)
wks.update_acell('C2', timestamp)
wks.update_acell('C3', timestamp)
wks.update_acell('C4', timestamp)
