#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

data = pd.read_csv('D:train.csv')
print(pd.DataFrame(data))


# In[7]:


print(data.to_string())


# In[8]:


#1. Display Top 5 Rows of The Dataset

data.head()


# In[10]:


# 2. Check the Last 3 Rows of The Dataset

data.tail(3)


# In[11]:


# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)

data.shape


# In[16]:


print("No of Rows",data.shape[0])


# In[18]:


print("No of Columns",data.shape[1])


# In[20]:


# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, 

data.info()


# In[22]:


# 5. Get Overall Statistics About The Dataframe

data.describe(include='all')


# In[23]:


# 6. Data Filtering

data.columns


# In[28]:


data[data['Sex'] == 'male']


# In[30]:


# 7.Check Null Values In The Dataset

data.isnull().sum()


# In[31]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[32]:


sns.heatmap(data.isnull())


# In[33]:


# 8. Drop the Column

data.drop("Cabin", axis = 1, inplace=True)


# In[34]:


data.isnull().sum()


# In[37]:


#9. Handle Missing Values

data["Embarked"].fillna('S', inplace=True)


# In[38]:


data.isnull().sum()


# In[39]:


data["Age"].fillna(data["Age"].mean(),inplace=True)


# In[41]:


data.isnull().sum()


# In[42]:


data


# In[43]:


# 10. Categorical Data Encoding
data.columns


# In[45]:


data["Sex"].unique()


# In[57]:


x=data["Sex"] = data["Sex"].map({'male':1,'female':0})


# In[59]:


data.insert(6, "New_Gender1",x)


# In[60]:


data


# In[ ]:




