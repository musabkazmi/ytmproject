import pandas as pd
# ye main dataframe hai
df = pd.read_csv("GIN-SELECTED.csv")
# ye copy dataframe
df1 = pd.DataFrame(columns = df.columns, 
                   index = df.index)
for x in df.COST_CENTER:
    # print("dd")
    dfname= "Cost_centre_" + str(x)
    dfname = df[df['COST_CENTER'] == x]
    dfname.to_csv(dfname + 'out.csv')

print(x)
# df1 = df[df['COST_CENTER'] == 90235]
# print(df1)
# #print(df.index.tolist())
# df1.to_csv('out.csv')