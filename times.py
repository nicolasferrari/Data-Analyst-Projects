from dateutil.parser import parse 
from datetime import datetime
import pandas as pd
import read
df = read.load_data()

# Write a function to extract the hour from a timestamp. The input is row and the parse function have the variable item passed.
def hour_time_stamp(row):
    
    item = row['submission_time']   
    item = parse(item)
    return item.hour
    
df['submission_hours'] =df.apply(hour_time_stamp, axis=1)

hour_occurrences = df['submission_hours'].value_counts()

print(hour_occurrences)
   
