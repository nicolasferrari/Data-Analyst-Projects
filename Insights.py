import sqlite3
import pandas as pd
conn = sqlite3.connect("factbook.db")
c = conn.cursor()

# Read the facts table into a Panda dataframe
facts = pd.read_sql_query("select * from facts;" ,conn)

# Filter out rows with missing values
facts = facts.dropna(axis=0)


# Query the database to observe the maximum and minimum of Population Density of the countries
query1 = "select name, (population)/(area) as Population_Density from facts order by Population_Density desc"
pop_density= conn.execute(query1).fetchall()
print(pop_density)
# We can observe that the country with the maximum population density is Macau, and the country with the minimum population density is Islas Malvinas

# The following query will show the country with the highest rate of migration
query2 = "select name, migration_rate from facts order by migration_rate desc;"
migration = conn.execute(query2).fetchall()
print(migration)
# The result of the query show that the country with the highest rate of migration is Qatar. In conclusion Qatar is the country that lose the highest amount of population for migration causes. There are a lots of countries with 0 rate of migration. Some of these countries are Andorra,Argentina,Belize,Japan,Serbia,South Korea. 
