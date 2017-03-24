import pandas as pd
data = pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")

#print(data["SCH_DISCWODIS_EXPWOE_HI_F"].sum())
#print(data["TOT_DISCWODIS_EXPZT_F"].sum())

expulsions =  ["SCH_DISCWODIS_EXPWOE_HI_M",
"SCH_DISCWODIS_EXPWOE_HI_F","SCH_DISCWODIS_EXPWOE_AM_M",
"SCH_DISCWODIS_EXPWOE_AM_F","SCH_DISCWODIS_EXPWOE_AS_M"
,"SCH_DISCWODIS_EXPWOE_AS_F",
"SCH_DISCWODIS_EXPWOE_HP_M","SCH_DISCWODIS_EXPWOE_HP_F",
     "SCH_DISCWODIS_EXPWOE_WH_M",
"SCH_DISCWODIS_EXPWOE_WH_F","SCH_DISCWODIS_EXPWOE_TR_M",
              "SCH_DISCWODIS_EXPWOE_TR_F","TOT_DISCWODIS_EXPZT_F"]


sum_of_expulsion = data[expulsions].sum()
print(sum_of_expulsion)
#print(exp_by_race.sum())
# Make a first Pivot Table to combine information of expulsion with state to observe the states that have the most higher number of expulsions
#expulsion_table = pd.pivot_table(data,values = expulsions, index = expulsions, aggfunc = "sum")
#print(expulsion_table)