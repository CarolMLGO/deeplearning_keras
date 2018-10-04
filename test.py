import matplotlib.pyplot as plt
import pandas as pd
import os
path='./t81_558_deep_learning/data/'
filename_read=os.path.join(path,'cgpa.csv')
df=pd.read_csv(filename_read)
print(df.head())