import sqlite3 as lite
import collections
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests

# selected cities
cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }

#Connect to API
### can you go over a little bit of how api_keys work? 
api_key = 'ewkdgvGnrePNwqGuKYtqUTsxEIGZgjAH'
url = 'https://api.forecast.io/forecast/' + api_key

# collecting past 30 days of data, end date is today
end_date = datetime.datetime.now()

#connect to weather.db database
con = lite.connect('weather.db')
cur = con.cursor()

#Create the table
with con: 
	cur.execute('CREATE TABLE daily_temp(day_of_reading INT, Atlanta REAL, Austin REAL, Boston REAL, Chicago REAL, Cleveland REAL);')

#start date 
query_date = end_date - datetime.timedelta(days=30)

#store the data 
with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)

#loop through cities and query API
for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #query for the value
        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))

        with con:
            #insert the temperature max to the database
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

        #increment query_date to the next day for next operation of loop
        query_date += datetime.timedelta(days=1) #increment query_date to the next day

#read the data into a dataframe
######## what does the con do in this line?
df = pd.read_sql_query('SELECT * FROM daily_temp', con, index_col = 'day_of_reading')

#close connection to database
con.close()

#######################################
#loop through to find range for each city
for i in df.columns:
	lower = min(df[i])
	upper = max(df[i])
	range = upper - lower
	print (i, range)

#find mean temperature for each city
for i in df.columns: 
	print(i, df[i].mean())

###### variance and largest temperature change

#plot line chart for each cities temp over past 30 days
pd.DataFrame.plot(df, kind='line')
