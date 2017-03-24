# Perform some analysis in the DF to find patterns
import pandas as pd
data = pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")

JJ_students = data["JJ"].value_counts()
magnet_school = data["SCH_STATUS_MAGNET"].value_counts()
print(JJ_students)
print(magnet_school)

# Construct two Pivot Tables 
pivot_1 = pd.pivot_table(data, values=["TOT_ENR_M","TOT_ENR_F"], index= "JJ", aggfunc="sum")
pivot_2 = pd.pivot_table(data, values=["TOT_ENR_M","TOT_ENR_F"], index= "SCH_STATUS_MAGNET", aggfunc="sum")
print(pivot_1)
print(pivot_2)
print(data.shape)
