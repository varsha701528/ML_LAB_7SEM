
# coding: utf-8

# In[2]:


import pandas as pd  
data = pd.read_csv('enjoy.csv')
columnLength= data.shape[1]
rowLength=data.shape[0]
print (data)
h=['0','0','0','0','0','0']
hp=[]
hn=[]
for i in range(rowLength):
    trainingExample=[]
    trainingExample.append(data.sky[i])
    trainingExample.append(data.airTemp[i])
    trainingExample.append(data.humidity[i])
    trainingExample.append(data.wind[i])
    trainingExample.append(data.water[i])
    trainingExample.append(data.forecast[i])
    if data.enjoySport[i]!='no':
        hp.append(trainingExample)
    else:
        hn.append(trainingExample)
for i in range (len(hp)):
    for j in range(columnLength-1):
        if (h[j]=='0'):
            h[j]=hp[i][j]
        if (h[j]!=hp[i][j]):
            h[j]='?'
        else:
            h[j]=hp[i][j]

print('\n')
print('The Maximally Specific Hypothesis h is')
print(h)

