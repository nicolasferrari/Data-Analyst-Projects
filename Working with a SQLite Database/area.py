# Query the facts table in the factbook database to compute the total area land, the total water land, and to get the ratio between land area and water area of the countries. 

import sqlite3
conn = sqlite3.connect("factbook.db")
c = conn.cursor()
query1 = "SELECT sum(area_land) from facts;"

land = conn.execute(query1).fetchall()
query2 = "SELECT sum(area_water) from facts;"
water = conn.execute(query2).fetchall()
query3 = "Select sum(area_land)/sum(area_water) from facts;"
total = conn.execute(query3).fetchall()
print(land)
print(water)
print(total)


