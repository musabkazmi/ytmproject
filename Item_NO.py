import pandas as pd
import datetime

d1 = datetime.datetime(2020, 1, 1)

df = pd.read_csv("40474.csv")
# ye function gindate ko date format mein convert kar raha hai
df['GINDATE']= pd.to_datetime(df['GINDATE'])
 
# df1 = pd.DataFrame(columns = ["ItemNo","Item_description","Jan"], 
#                    index = df.index)

#YE KHAS  ITEM NO KO ALAG KARE GA
dfname = df[df['ITEMNO'] == 18873 ]
#YE KHAS  DAATE KO FILTER KARE 
dfname = dfname[dfname['GINDATE'] > d1]
# print(dfname.at[36,'QUANTITY'])
print(dfname.ITEMNO)
# dfname = df[df['ITEMNO'] == 18920]
# print(dfname)
df1 = pd.DataFrame(columns = ["ITEMNO","Item_description","year","Jan","Feb","March","Aprill","May","june","July","August","Sep","Oct","Nov","Dec",]
                    )
df1.at[1,'ITEMNO']= dfname.at[36,'ITEMNO']
sumquantity = dfname.QUANTITY 
l2=tuple(sumquantity)
print(sum(l2))
#print(df.at[0,'ITEM_CTG_ID'])
#dfname = df[df['COST_CENTER'] == x]
# Now we will check the data type
# of the 'Date' column
#df.info()


