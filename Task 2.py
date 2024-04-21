#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data=pd.read_csv(r'C:\Users\pc\Documents\Heart Disease\Heart_Disease_Prediction.csv')


# In[5]:


display(data.head())


# In[ ]:


# Finding out Missing values


# In[6]:


print(data.isnull().sum())


# In[7]:


# There is no missing values in the data set


# In[8]:


#Now filtering by specific conditions 


# In[14]:


# 1.Filtering by age 
children = data[data['Age']<13]
Teen = data[(data['Age']>=13) & (data['Age']<20)]
Adult = data[(data['Age']>=20) & (data['Age']<=50)]
Senior_citizen = data[data['Age']>50]


# In[19]:


print(children['Age'].count())
print(Teen['Age'].count())
print(Adult['Age'].count())
print(Senior_citizen['Age'].count())


# In[22]:


# 2.Filter by those with Heart Disease
present=data[data['Heart Disease']=='Presence']
print(present['Heart Disease'].count())


# In[24]:


# Summary Statistics
print(data.describe())


# In[ ]:




