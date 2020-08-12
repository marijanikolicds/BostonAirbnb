#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Read necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


# Read data
df = pd.read_csv('data/listings.csv')
print(df.shape)
df.head()


# In[7]:


# What is the distribution of properties across neighbourhoods?
neighbourhood_values = df.neighbourhood.value_counts()
plt.figure(figsize=(10,10))
(neighbourhood_values/df.shape[0]).plot(kind="bar");
plt.title("What is the distribution of properties across neighbourhoods?");
plt.ylabel('Frequency');
plt.xlabel('Neighbourhoods');


# In[16]:


# Properties in which neighborhoods are associated with the best scores for location (mean value)
df.groupby('neighbourhood').review_scores_location.agg([min, max, pd.Series.mean, pd.Series.mode]).sort_values('mean', ascending = False)


# In[9]:


# What types of properties are available in Boston Airbnb and what are their shares?
values = df.room_type.value_counts()
plt.figure(figsize=(10,10))
(values/df.shape[0]).plot(kind="bar");
plt.title("What types of listings are available in Boston Airbnb and what are their shares?");
plt.ylabel('Frequency');
plt.xlabel('Property type');


# In[10]:


# What is the distribution of scores for cleanliness?
values = df.review_scores_cleanliness.value_counts()
plt.figure(figsize=(10,10))
(values/df.shape[0]).plot(kind="bar");
plt.title("What is the distribution of scores for cleanliness?");
plt.ylabel('Frequency');
plt.xlabel('Score');


# In[21]:


# What are the best neighborhoods to choose in terms of location of the property and its privacy and cleanliness
df_filtered = df[(df.room_type.isin(['Private room', 'Entire home/apt'])) & (df.review_scores_cleanliness == 10)]
df_filtered.groupby(['neighbourhood']).review_scores_location.agg([min, max, pd.Series.mean, pd.Series.mode]).sort_values('mean', ascending = False)


# In[30]:


# What is the best accomodation by neighbourhood and room type?
# # Remove rows with missing values in column 'review_scores_value'
df_filtered = df[(df.room_type.isin(['Private room', 'Entire home/apt'])) &                  df.neighbourhood.isin(['Financial District', 'Brookline', 'Chestnut Hill', 'Government Center]'])]                  .dropna(subset = ['review_scores_value'], how = 'any')

ans = df_filtered.groupby(['neighbourhood', 'room_type']).apply(lambda x: x.loc[x.review_scores_value.idxmax()])
ans[['neighbourhood','room_type', 'name', 'description','review_scores_value']]


# In[ ]:


# Additional analyses


# In[31]:


#W hat is the average score for each room type category?
df.groupby('room_type').review_scores_value.mean()


# In[32]:


# What is the average score for each neighbourhood?
df.groupby('neighbourhood').review_scores_value.mean()


# In[19]:


# Are there significant differences in the average scores assigned to different room types?
df.groupby('room_type').review_scores_value.describe()


# In[ ]:


# What combinations of neighbourhood and room types are most common?
df.groupby(['neighbourhood', 'room_type']).size().sort_values(ascending = False).head(20)

