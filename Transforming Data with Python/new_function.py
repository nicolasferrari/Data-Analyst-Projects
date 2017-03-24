import pandas as pd
from pandas import Series
import read
import numpy as np 

hn_stories = read.load_data()

# Find what year has the highest number of upvotes?
# This function extract the year from the submission_time column to make a new column name submission_year that contain the year of the url upvote.
def get_first_chart(submission_time):
    return submission_time[0:4]
hn_stories['submission_year'] = hn_stories['submission_time'].apply(get_first_chart) 
print(hn_stories['submission_year'].value_counts())

#With the value counts over the submision_year column is possible to observe the number of upvotes that each year has. The year with the most upvoted times was 2013 with 1902.

# In the second point, I find what headline length leads to the most upvotes?
# First I make a function to calculate the len of each row in the headline column
def len_headline(row):
    headline = row['headline']
    str_headline = str(headline)
    len_headline = len(str_headline) 
    return len_headline
hn_stories['len_headline'] = hn_stories.apply(len_headline,axis=1)
print(hn_stories['len_headline']) 

# Second use a pivottable to find the  mean of upvotes for each headline len

headline_len_to_upvotes = hn_stories.pivot_table(index= 'len_headline', values = 'upvotes')

order = headline_len_to_upvotes.copy().sort_values()
print(order)
# The headline lenght with the most upvotes is 67 lenght with a mean of 19.5 upvotes. In contrast the headline lenght with the least upvotes is 97 with one. 

# Find what submission time leads to the most upvotes. For this, I make a pivot table with the time hour as index and upvotes with values.

submission_hour_to_upvotes = hn_stories.pivot_table(index= 'submission_time', values = 'upvotes')

order_submission = submission_hour_to_upvotes.copy().sort_values()
print(order_submission)
 
# The submission time with the most upvotes was on 2012-02-15T21:22:35Z with 789 upvotes
