#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("study_performance.csv")
print(df.head())


# In[3]:


df.describe()


# In[4]:


df.info


# In[6]:


df.isnull().sum()


# In[7]:


df.head()


# # gender Distribution

# In[33]:


plt.figure(figsize= (5,5))
ax = sns.countplot(data = df, x = "gender")
ax.bar_label(ax.containers[0])
plt.title("Gender distribution")
plt.show()


# In[23]:


# from the above chart we have analysed that:
#the number of female in the data is more than the number of males


# In[31]:


gb = df.groupby("parental_level_of_education").agg({"math_score":'mean',"reading_score":'mean',"writing_score":'mean'})
print(gb)


# In[35]:


plt.figure(figsize= (4,4))
sns.heatmap(gb, annot = True)
plt.title("Relationship between Prental Education and Student's Score")
plt.show()


# In[32]:


# from the above chart we have concluded that the education of the parents have a good impacts on their scores.


# In[36]:


sns.boxplot(data = df, x = "math_score")
plt.show


# In[37]:


sns.boxplot(data = df, x = "reading_score")
plt.show


# In[38]:


sns.boxplot(data = df, x = "writing_score")
plt.show


# In[39]:


print(df["race_ethnicity"].unique())


# # Distribution of Ethinic Groups

# In[55]:


groupA = df.loc[(df['race_ethnicity'] == "group A")].count()
groupB = df.loc[(df['race_ethnicity'] == "group B")].count()
groupC = df.loc[(df['race_ethnicity'] == "group C")].count()
groupD = df.loc[(df['race_ethnicity'] == "group D")].count()
groupE = df.loc[(df['race_ethnicity'] == "group E")].count()

l = ["groupA", "groupB", "groupC", "groupD", "groupE"]
mlist = [groupA['race_ethnicity'], groupB['race_ethnicity'], groupC['race_ethnicity'], groupD['race_ethnicity'], groupE['race_ethnicity']]
print(mlist)
plt.pie(mlist, labels = l, autopct = "%1.2f%%")
plt.title("Distribution of Ethenic Groups")
plt.show


# In[54]:


ax = sns.countplot(data = df, x = 'race_ethnicity')
ax.bar_label(ax.containers[0])


# In[ ]:




