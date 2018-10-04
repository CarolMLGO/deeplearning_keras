import os 
import pandas as pd
import numpy as np
# print(pd.__version__)
pd.set_option('display.expand_frame_repr', False)
path='./data/'
filepath_read=os.path.join(path,'auto-mpg.csv')
filepath_write=os.path.join(path,'write-out.csv')
df=pd.read_csv(filepath_read)
# df.to_csv(filepath_write,index=True)
# print(df.head())

#perform some basic statistics
df=df.select_dtypes(include=['int','float'])
headers=list(df.columns.values)
print(headers)


