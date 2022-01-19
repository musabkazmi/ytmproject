import pandas as pd
#df = pd.read_csv("GIN 1-1-19 to 29-11-21.csv")
df = pd.read_csv("GIN-SELECTED.csv")
#print(df.at[4,'ITEMNO'])
l = (df.COST_CENTER)
l1= (set(l))
#x= l1.count(5)
l2=tuple(l1)

# l2df = pd.DataFrame(l2,columns = ['ITEMNO'])
# rslt_df = l2df[l2df['ITEMNO'] == 8177]
#df = l2df[l2df['COST_CENTER'] == 8177]
#l2['ITEMNO']== 8177
print(len(l2))
print(l2)
