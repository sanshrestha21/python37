import pandas as pd
#create a data frame - dictionary is used here where keys get converted to column names and values to row values.
data = pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
                    'Rank':[121,40,100,130,11]})

print(data)
print(data.describe())
print(data.info())
sorted=data.sort_values(by=['Rank'],ascending=True,inplace=False)
print(sorted)
data=pd.DataFrame({'Country':['Nepal']*3+['Bhutan']*4,'Rank':[198,186,454,280,231,111,55]})
print(data)