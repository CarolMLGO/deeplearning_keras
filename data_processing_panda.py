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

######perform some basic statistics
# df=df.select_dtypes(include=['int','float'])
# headers=list(df.columns.values)
# print(headers)

######Sorting, shuffling dataframes
np.random.seed(1)
df=df.reindex(np.random.permutation(df.index))
# df.reset_index(inplace=True,drop=True)

# mask=np.random.rand(len(df))<0.8
# train_df=pd.DataFrame(df[mask])
# val_df=pd.DataFrame(df[~mask])
# print(train_df[0:10])

# print(f'Trianing set: {len(train_df)}')
# print(f'Validation set:{len(val_df)}')

#####K-fold validation
from sklearn.model_selection import KFold
kf=KFold(5)
fold=1
for train_index,validate_index in kf.split(df):
    train_df=pd.DataFrame(df.iloc[train_index,:])
    validate_df=pd.DataFrame(df.iloc[validate_index])
    print(f'Training set: {len(train_df)}; validation set: {len(validate_df)}')
    fold+=1






