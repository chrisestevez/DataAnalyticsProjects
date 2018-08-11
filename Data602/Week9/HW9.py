# -*- coding: utf-8 -*-

import pandas as pd
import re

#Loading data into pandas
Data = pd.read_table('epa-http.txt', header=None, squeeze=True, sep='\s+', na_values="-",
                     names=['Host', 'Date', 'Request', 'HTTP_code', 'bytes']
                     )

# I Replaced NAs with 0s
Data = Data.fillna(0)
#Formated date time field
Data['Date'] = pd.to_datetime(Data['Date'], format='[%d:%H:%M:%S]')

print "-"*100
print "hostname or IP address made the most requests?"
print "The hostname with the most request is "
Most_Requests = Data.groupby(by='Host')['Host'].count().sort_values(ascending=False).head(n=1)

print Most_Requests

print "-"*100
print "Which hostname or IP address received the most total bytes from the server? How many bytes did it received?"
print "The hostname with the most total bytes is "

Most_bytes = Data.groupby(by='Host')['bytes'].sum().sort_values(ascending=False).head(n=1)

print Most_bytes

print "-"*100
print "what hour was the server the busiest in terms of requests?  (You can do this by grouping each hour period"
print "e.g. 13:00 – 14:00. Then count the number of requests in each hour)"

Hours = pd.DataFrame({'Hour': Data['Date'].dt.hour})

Busy_hour = Hours.groupby(by='Hour')['Hour'].count().sort_values(ascending=False)
print "The busiest hours for the the server are "

print Busy_hour

print "-"*100
print"Which .gif image was downloaded the most during the day?"

imgs = Data[(Data['HTTP_code'] == '200') & (Data.Request.str.contains('.gif'))]

imgs = imgs.groupby(by='Request')['Request'].count().sort_values(ascending=False).head(n=1)

#Tried to extract using regex
#result = re.findall(r'\{2,}(\+gif)$', imgs)

print "The most downloaded gif image is "
print imgs


print "-"*100
print "What HTTP reply codes were sent other than 200?"
print "Codes other than 200 are "


Other_codes = Data[(Data.HTTP_code != '200') & (Data.HTTP_code != 'HTTP/1.0"')]

Other_codes = Other_codes.groupby(by='HTTP_code')['HTTP_code'].count().sort_values(ascending=False)


print Other_codes

