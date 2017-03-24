# Set the environment to work with SQLite and      Python. First, import the sqlite3 library that   allows us to connect to SQLite databases.          Secondly, open a database connection, then      create an object that can run queries.
# Write a query that select the 10 countries with the least population from the facts table, and print the results.

import sqlite3
conn = sqlite3.connect("factbook.db")
c = conn.cursor()
query = "SELECT name,population FROM facts order by population asc LIMIT 10;"
c.execute(query)
print(c.fetchall())

