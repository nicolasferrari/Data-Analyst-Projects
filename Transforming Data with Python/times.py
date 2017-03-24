from dateutil.parser import parse 
from datetime import datetime
import pandas as pd
import read
df = read.load_data()

# This task consist in writing a function to extract the hour from a timestamp and find when are the most articles submitted. For this, I use the dateutil library with the parse function that take in a timestamp, and return a datetime object. 

# The hour property of the resulting date object will tell the hour the article was submitted.

# Use the pandas apply method to make a column of submission hours and the value_counts method to find the number of occurrences of each hour.

def hour_time_stamp(row):
    
    item = row['submission_time']   
    item = parse(item)
    return item.hour
    
df['submission_hours'] =df.apply(hour_time_stamp, axis=1)

hour_occurrences = df['submission_hours'].value_counts()

print(hour_occurrences)

# The 17 hour is the most submitted. 
#This procedure can be repeat to find how many articles were submitted on each day or the month, year, minute, day of the week and so on.  


  
