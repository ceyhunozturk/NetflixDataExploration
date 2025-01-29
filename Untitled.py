#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

df=pd.read_csv("Netflix.csv")


# In[9]:


# to show top-5 records of the dataset

df.head()


# In[12]:


# to show bottom-5 records of the dataset

df.tail() 


# In[14]:


# to show the No. of Rows and Columns

df.shape


# In[15]:


# to show No. of total values(elements) in the dataset

df.size


# In[17]:


# to show each column name

df.columns


# In[19]:


# to show the data-type of each column

df.dtypes


# In[21]:


# to show indexes, columns, data types of each column,memory at once

df.info()


# ### Task 1.Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.

# In[23]:


df[df.duplicated()]


# In[26]:


df.drop_duplicates(inplace=True)


# In[27]:


df[df.duplicated()]


# ### Task 2.Is there any Null value present in any column ? Show with heatmap.

# In[28]:


df.head()


# In[30]:


df.isnull().sum()


# In[32]:


import seaborn as sns

sns.heatmap(df.isnull())


# ### Q.1. For 'House of Cards', what is the Show Id and Who is the director of this show? 

# In[43]:


df[df['Title'].str.contains('House of Cards')]


# ### Q.2 In which year highest number of TV Shows & Movies were released ? Show with Bar Graph

# In[50]:


df['Release_Date']=pd.to_datetime(df['Release_Date'])


# In[53]:


df['Release_Date'].dt.year.value_counts()


# In[55]:


df['Release_Date'].dt.year.value_counts().plot(kind='bar')


# ### Q.3 How many Movies & TV Shows are in dataset? Show with Bar Graph.

# In[62]:


df.groupby("Category")['Category'].count()


# In[64]:


sns.countplot(data=df, x='Category')


# ### Q.4. Show all the Movies that were released in year 2000

# In[73]:


df[(df['Release_Date'].dt.year==2020) & (df['Category']=='Movie')]


# ### Q.5. Show only the Titles of all Movies that were released in Turkey

# In[97]:


df[(df["Country"]=='Turkey') & (df['Category']=='Movie')]


# ### Q.6 Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix

# In[101]:


df['Director'].value_counts().head(10)


# ### Q.7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom"

# In[103]:


df[(df["Category"]=='Movie') & (df["Type"].str.contains('Comedies')) | (df['Country']=='United Kingdom')]


# ### Q.8. In how many movies/shows, Tom Cruise was cast ?

# In[114]:


df_new=df.dropna()


# In[117]:


df_new[df_new["Cast"].str.contains('Tom Cruise')]


# ### Q.9. What are the different Ratings defined by Netflis?

# In[121]:


df["Rating"].nunique()


# ### Q.9.1. How many Movies got the 'TV-14' rating, in Canada ?

# In[126]:


df[(df["Category"]=='Movie') & (df['Rating']=='TV-14')  &  (df['Country']=='Canada')].shape


# ### Q.10. What is the maximum duration of a Movie/Show on Netflix ?

# In[149]:


df[['Minutes','Unit']] = df['Duration'].str.split(' ',expand = True)


# In[156]:


df['Minutes']=df['Minutes'].astype(int)
df['Minutes'].max()


# ### Q.11. Which individual country has the Highest No. of TV Shows ?

# In[167]:


df_tvshow=df[df['Category']=='TV Show']
df_tvshow.Country.value_counts()


# ### Q.12. How can we sort the dataset by Year?

# In[169]:


df.sort_values(by='Release_Date',ascending=False)


# In[ ]:




