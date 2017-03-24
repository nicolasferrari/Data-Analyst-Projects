import pandas as pd
import string 

#Read the file hn_stories.csv and add column names
hn_stories = pd.read_csv("hn_stories.csv")
hn_stories.columns = ['submission_time','upvotes','url','headline']

# Obtain the number of times each domain is submitted in the data set. For this purpose, I use the value_counts method to observe the domain variable with the name of the domain as the index, and the number of times that was submitted as the value.
domains = hn_stories['url']

domains.value_counts()
# Print the 100 most submitted domains
print(domains.value_counts().head(100))

def remove_subdomain(col):
    new_url = '.'.join(col.split('.')[-2:])
    return new_url
hn_stories['new_domain'] = hn_stories['url'].apply(remove_subdomain)
print(hn_stories['new_domain'])