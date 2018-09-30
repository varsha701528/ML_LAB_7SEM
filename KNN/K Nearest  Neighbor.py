
# coding: utf-8

# In[10]:


import numpy as np
from sklearn.datasets import load_iris 
iris=load_iris()


x=iris.data 
y=iris.target
print(x[:5],y[:5]) 


# In[11]:


from sklearn.model_selection import train_test_split 

xtrain,xtest,ytrain,ytest =train_test_split(x,y,test_size=0.4,random_state=1)

print(iris.data.shape) 

print(len(xtrain)) 

print(len(ytest))


# In[12]:


from sklearn.neighbors import KNeighborsClassifier 

knn=KNeighborsClassifier(n_neighbors=5) 

knn.fit(xtrain,ytrain)


pred=knn.predict(xtest)


# In[13]:


from sklearn import metrics 
print(metrics.accuracy_score(ytest,pred))



# In[14]:


print(iris.target_names[2]) 
ytestn=[iris.target_names[i] for i in ytest]
predn=[iris.target_names[i] for i in pred]



# In[15]:


print("  predicted     Actual")
for i in range(len(pred)):
    print(i," ",predn[i],"   ",ytestn[i]) 

