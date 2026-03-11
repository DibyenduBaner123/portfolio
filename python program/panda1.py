import pandas as pd
x=[3,4,5,6]
var=pd.Series(x,index=['a','b','c','d'])
print(var)
print(type(var))
print(var.iloc[3])
print(var.loc['d'])
