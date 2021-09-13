#!/usr/bin/env python
# coding: utf-8

# # THE SPARKS FOUNDATON 
# ## TASK 4

# In[2]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


dataset=pd.read_csv('terror_dataset.csv',encoding='latin')
dataset.head()


# In[4]:


dataset.info(object)


# SELECT THE IMPORT COLUMNS NEEDED FOR EDA

# In[5]:


df=dataset[['iyear','imonth','iday','extended','country_txt','region_txt','provstate','summary','location','attacktype1_txt',
           'targtype1_txt','natlty1_txt','gname','nperps','weaptype1_txt','nkill','nwound']]


# In[6]:


sns.heatmap(df.isnull())


# In[7]:


df.isnull().sum()


# In[8]:


df.describe()


# In[9]:


df.head()


# In[10]:


print('Country with most terror attack happened is', df['country_txt'].value_counts().idxmax())


# In[11]:


print('Country with less terror attack happened is', df['country_txt'].value_counts().idxmin())


# In[12]:


print('State with most terror attack happened is', df['provstate'].value_counts().idxmax())


# In[13]:


country=df['country_txt'].value_counts()[0:15]
country


# # Visualization

# In[14]:


plt.subplots(figsize=(10,10))
plt.xticks(rotation=45)
plt.title('MOST AFFECTED COUNTRIES')
sns.barplot(x=country.index,y=country.values)


# In[15]:


year=df['iyear'].unique()
count=df['iyear'].value_counts().sort_index()


# In[16]:


plt.subplots(figsize=(20,10))
plt.xticks(rotation=45)
plt.title('Yesr wise terror attacks')
sns.barplot(x=year,y=count)


# Most Terror attacks is happened on 2014

# In[17]:


d=df.groupby('country_txt')['nkill'].sum()[0:15]


# In[18]:


d.index


# In[19]:


plt.subplots(figsize=(20,10))
plt.xticks(rotation=45)
plt.title('Country where most people killed by terror attack')
sns.barplot(x=d.index,y=d.values)


# In[20]:


w=df.groupby('country_txt')['nwound'].sum()[0:15]


# In[21]:


plt.subplots(figsize=(20,10))
plt.xticks(rotation=45)
plt.title('Country where most people wounded by terror attack')
sns.barplot(x=w.index,y=w.values)


# In[26]:


attack_country = dataset['nwound'].value_counts()[:15]
attack_country


# In[30]:


attack_wounded = dataset[['attacktype1_txt','nwound']].groupby(["attacktype1_txt"],axis=0).sum()
attack_wounded


# In[33]:


plt.subplots(figsize=(12,6))
plt.xticks(rotation=45)
sns.barplot(attack_wounded.index, attack_wounded.nwound.values,palette="viridis")


# In[ ]:




