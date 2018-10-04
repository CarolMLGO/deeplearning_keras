import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
path='./data/'
filename_read=os.path.join(path,'cgpa.csv')

df=pd.read_csv(filename_read)
data=df.head(100)
x=data['rollno']
y=data['cgpa']

fig=plt.figure()
fig.patch.set_facecolor("gray")
ax1=fig.add_subplot(1,2,1,facecolor="yellow")
ax1.plot(x,y)

fig=plt.figure()
x1=len(data[data.cgpa>=9])
x2=len(data[(data.cgpa>=8)&(data.cgpa<9)])
x3=len(data[data.cgpa<8])
ax2=fig.add_subplot(111)
ax2.axis('equal')
ax2.pie([x1,x2,x3],colors=["yellow",'green','red'],labels=['9 pts','8 pts','others'])
ax2.legend(title="description")



# plt.plot(data['rollno'],data['cgpa'],color="orange",label="line graph")
# plt.bar(data['rollno'],data['cgpa'],color=["green","blue","red"])
# plt.legend()
# plt.xlabel("Roll No",color="green")
# plt.ylabel("CGPA",color="blue")
# plt.title("CGPA VS Roll No",color="green")
plt.show()


