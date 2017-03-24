import pandas as pd 
import sqlite3
import math
conn = sqlite3.connect("factbook.db")
# Read the facts table into a Panda dataframe
facts = pd.read_sql_query("select * from facts;" ,conn)

# Filter out rows with missing values
facts = facts.dropna(axis=0)

# The function final_pop calculate the popoulation of each country over 35 years. For this, takes in the initial population, the growth rate of a country and output the final population.

def final_pop(row):
    r = row['population_growth']/100
    N0 = row['population']
    e = math.e
    final_population = N0*e**(r*35)
    return round(final_population,0)
facts['Population_2050'] = facts.apply(final_pop,axis=1)
facts_order = facts['Population_2050'].sort_values(ascending = False)

print(facts_order.head(10))
print(facts['Population_2050'])


# Create a function to find out which countries will lose population over the next 35 years. For that, I take the population in 2050 minus the population today times the migration rate in 35 years. If this value is less than the population today, means that the country will lose population.  

def lose_population(row):
    if row['Population_2050'] - (((row['migration_rate'] / 100) * 35) *  row['population']) < row['population']:
        return 'YES'
    else:
        return 'NO'
facts['Will_lose_population?'] = facts.apply(lose_population,axis=1)
# Print all the rows of the facts datafram for the countries that will lose population: 
print(facts[facts['Will_lose_population?'] == 'YES'])

