#!/usr/bin/env python
# coding: utf-8

# In[1]:


python -- version


# In[2]:





# In[4]:


from platform import python_version
print(python_version())


# In[10]:


import pandas as pd
data = pd.read_csv("D:\Python\Ecommerce Purchases.csv")
data.head(10)


# In[11]:


data.tail(10)


# In[13]:


data.dtypes


# In[15]:


data.isnull().sum()


# In[18]:


len(data.columns)


# In[27]:


import pandas as pd
data = pd.read_csv("D:\Python\RN.csv")
df = pd.DataFrame(data)
print(df)


# In[28]:


print(data.to_string())


# In[29]:


data


# In[30]:


data.tail(10)


# In[31]:


data.head(10)


# In[34]:


data.dtypes


# In[36]:


data.isnull().sum()


# In[37]:


data


# In[43]:


len(data.columns)


# In[44]:


len(data)


# In[46]:


data.info()


# In[47]:


data.columns


# In[49]:


data["Lentgthkm"]


# In[50]:


data["Lentgthkm"].sum()


# In[53]:


data["Lentgthkm"].max()


# In[54]:


data["Lentgthkm"].min()


# In[55]:


data["Lentgthkm"].mean()


# In[56]:


data.columns()


# In[57]:


data.columns


# In[58]:


data["REV_CAT"]


# In[60]:


[data["REV_CAT"]=="D1"]


# In[61]:


len(data[data["REV_CAT"]=="D1"])


# In[63]:


data[data["REV_CAT"]=="D1"].count()


# In[64]:


data


# In[ ]:




