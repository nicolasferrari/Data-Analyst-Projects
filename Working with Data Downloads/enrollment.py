import pandas as pd 
data = pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")

# Create a column that adds the total enrollment by male(TOT_ENR_M) and total enrollment by female(TOT_ENR_F) columns.
data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]


columns = ["SCH_ENR_HI_M","SCH_ENR_HI_F","SCH_ENR_AM_M",
"SCH_ENR_AM_F","SCH_ENR_AS_M","SCH_ENR_AS_F",     "SCH_ENR_HP_M","SCH_ENR_HP_F","SCH_ENR_BL_M",
"SCH_ENR_BL_F", "SCH_ENR_WH_M","SCH_ENR_WH_F","SCH_ENR_TR_M",
"SCH_ENR_TR_F"]
sum_columns = data[columns].sum()
print(sum_columns)
all_enrollment = data["total_enrollment"].sum()
print("Sum of total enrollment:", all_enrollment)

# Figure out what percentage of enrollment each race/gender group is.

print(sum_columns / all_enrollment)

# It will be interesting to observe information about expulsions of students in schools. For that task I will be looking columns SCH_DISCWODIS_EXPWOE_HI_M and TOT_DISCWODIS_EXPZT_F

