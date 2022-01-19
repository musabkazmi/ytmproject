from enum import unique
import pandas as pd
import datetime

df_main = pd.read_csv("40474.csv")
# ye function gindate ko date format mein convert kar raha hai
df_main['GINDATE']= pd.to_datetime(df_main['GINDATE'])

# yaha tuple banega unique itemno ka
item_no_series = (df_main.ITEMNO)
unique_item_no_series= (set(item_no_series))
unique_item_no_tuple=tuple(unique_item_no_series)

#yaha date baane gi 2019 jan se 2021 dec tak
date_list = []
for i in (2019,2020,2021):
    for j in range(1,13):
        date_list.append(datetime.date(i, j, 1))

# yaha naya data frame banea JIS ME  final csv banega

df_final = pd.DataFrame(columns = ["ITEMNO","INV_ITEM_DESCRIPTION","Year","Jan","Feb","March","April","May","June","July","August","Sep","Oct","Nov","Dec",]
                    )

# print(df_main.columns)
index = 100
print(df_final)
df_final.at[index,'ITEMNO']= 999
print(df_final)
for i in unique_item_no_tuple:
    for j in date_list:
        # rslt_df = l2df[l2df['ITEMNO'] == 8177]
        df_final.at['ITEMNO']= i


