import pandas as pd
data = pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")

sat_scores = ["SCH_SATACT_HI_M","SCH_SATACT_HI_F","SCH_SATACT_AM_M",
"SCH_SATACT_AM_F","SCH_SATACT_AS_M","SCH_SATACT_AS_F",
"SCH_SATACT_HP_M","SCH_SATACT_HP_F","SCH_SATACT_BL_M",
"SCH_SATACT_BL_F","SCH_SATACT_WH_M","SCH_SATACT_WH_F",
"SCH_SATACT_TR_M","SCH_SATACT_TR_F"]

average_sat_score = data[sat_scores].mean()
print(average_sat_score)