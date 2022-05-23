#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

data = pd.read_csv("D:adult.csv")


# In[5]:


data


# In[6]:


# 1.Display Top 10 Rows of The Dataset

data.head(10)


# In[7]:


data.tail(10)


# In[9]:


# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)

data.shape


# In[13]:


print("No of Rows", data.shape[0])


# In[15]:


print("No of Columns", data.shape[1])


# In[17]:


# 4. Getting Information About Our Dataset Like Total Number Rows, 
#Total Number of Columns, Datatypes of Each Column And Memory Requirement

data.info()


# In[18]:


# 5. Fetch Random Sample From the Dataset (50%)

data.sample(frac=0.5)


# In[20]:


# 6.Check Null Values In The Dataset

data.isnull().sum()


# In[22]:


#7.Perform Data Cleaning [ Replace '?' with NaN ]
data.tail(20)


# In[23]:


data.isin(["?"]).sum()


# In[24]:


data.columns


# In[25]:


data['workclass']=data['workclass'].replace('?',np.nan)
data['occupation']=data['occupation'].replace('?',np.nan)
data['native-country']=data['native-country'].replace('?',np.nan)


# In[26]:


data


# In[28]:


data.isin(["?"]).sum()


# In[29]:


data.isnull().sum()


# In[30]:


# 8. Drop all The Missing Values

data.dropna(how='any',inplace = True)


# In[32]:


data.shape


# In[33]:


48842-45222


# In[34]:


data


# In[36]:


data.isnull().sum()


# In[37]:


#9. Check For Duplicate Data and Drop Them

data.duplicated().any()


# In[40]:


data=data.drop_duplicates()


# In[41]:


data.shape


# In[42]:


# 10 Get overall statistics of the DataFrame

data.describe()


# In[44]:


# 11. Drop The Columns education-num, capital-gain, and capital-loss

data.columns


# In[47]:


data=data.drop(["educational-num","capital-loss","capital-gain"], axis=1)


# In[48]:


data.columns


# In[49]:


# 12. What Is The Distribution of Age Column?

data["age"].describe()


# In[51]:


data["age"].hist()


# In[53]:


# 13. Find Total Number of Persons Having Age Between 17 To 48 (Inclusive) Using Between Method

sum(data["age"].between(17,48))


# In[54]:


# 14. What is The Distribution of Workclass Column?

data.columns


# In[59]:


data['workclass'].hist()


# In[60]:


# 15. How Many Persons Having Bachelors and Masters Degree?

data.columns


# In[67]:


x = len(data['education']=='Bachelors')
y = len(data['education']=='Masters Degree')

z=x+y

print(z)

sum(data['education'].isin(['Bachelors','Masters Degree']))


# In[68]:


# 16. Bivariate Analsis
# 17. Replace Salary Values With 0 and 1

data.columns


# In[71]:


def income_data(sal):
    if sal  =='<=50K':
        return 0
    else:
        return 1
data['salary_code'] = data["income"].apply(income_data)
    


# In[72]:


data.head()


# In[73]:


data.replace(to_replace=["<=50K",">50K"], value=[0,1], inplace = True)


# In[76]:


data.head(1)


# In[77]:


data


# In[78]:


#18. Which Workclass Getting The Highest Salary?

data.columns


# In[81]:


data.groupby('workclass')['income'].mean().sort_values(ascending = False)


# In[84]:


# 19.How Has Better Chance To Get Salary greater than 50K Male or Female?
data.groupby('gender')['income'].mean().sort_values(ascending=False)


# In[85]:


#20. Covert workclass Columns Datatype To Category Datatype
data.columns


# In[89]:


data["workclass"]=data["workclass"].astype('category')


# In[90]:


data.info()


# In[ ]:




