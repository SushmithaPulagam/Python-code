#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Read the diamond file
import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\VIAAN\\Desktop\\Kaggle Competitions\\diamonds.csv")


# In[2]:


# Read the first 5rows
df.head(6)


# In[3]:


# Extracting only selected columns

col_names = ['carat','cut']
df[col_names].head(6)


# In[6]:


#select a series from diamonds DataFrame. Print the content of the series.

df['carat'].head(6)


# In[10]:


#create a new 'Cut -color' Series (use bracket notation to define the Series name) of the diamonds DataFrame

df['Cut-Color'] = df.cut+','+df.color


# In[11]:


df.head(6)


# In[14]:


# find the number of rows and columns and data type of each column of diamonds Dataframe. 

df.shape


# In[15]:


df.dtypes


# In[16]:


# summarize only 'object' columns of the diamonds Dataframe

df.describe(include = ['object'])


# In[20]:


# rename two of the columns of the diamonds Dataframe

df.rename(columns = {'cut':'Cut', 'color':'Color'})


# In[26]:


# remove the second column of the diamonds Dataframe

df.drop('cut',axis = 1,inplace = False)


# In[27]:


df.head(5)


# In[25]:


# remove multiple columns at once of the diamonds Dataframe 

df.head(6)


# In[28]:


df.head(5)


# In[30]:


df.drop('Cut-Color',axis=1,inplace = False).head(6)


# In[31]:


df.head(6)


# In[34]:


df.head(6)


# In[35]:


df.columns


# In[36]:


df.drop('Unnamed: 0',axis =1, inplace=True)


# In[37]:


df.head(6)


# In[38]:


df.columns


# In[39]:


df.drop('z',axis =1, inplace=False)


# In[41]:


df.columns


# In[42]:


#sort the 'cut' Series in ascending order (returns a Series) of diamonds Dataframe.

result = df.cut.sort_values(ascending = True)


# In[44]:


print (result)


# In[45]:


# sort the 'price' Series in descending order (returns a Series) of diamonds Dataframe.

result1 = df.price.sort_values()


# In[46]:


print(result1)


# In[47]:


df.head(6)


# In[48]:


#load the data again

df1 = pd.read_csv("C:\\Users\\VIAAN\\Desktop\\Kaggle Competitions\\diamonds.csv")


# In[49]:


df1.columns


# In[51]:


df1[df1.carat > 0.3]


# In[52]:


# program to convert a python list to pandas series

my_list = [1,3,4,5,7]
s=pd.Series(my_list)
s


# In[53]:


# program to find the details of the diamonds where length>5, width>5 and depth>5. 


df1.head(6)




# In[54]:


r = df1[(df1.x >5)& (df1.y >5) &(df1.z >5) ]


# In[56]:


r.shape


# In[59]:


# find the diamonds that are either Premium or Ideal.

df1[(df1.cut == 'Premium') | (df1.cut == 'Ideal')]


# In[60]:


# find the diamonds that are with a Fair or Good or Premium

df1[(df1.cut == 'Fair') | (df1.cut == 'Good')|(df1.cut == 'Premium')]


# In[64]:


# another syntax for multi s=conditions

df1[df1.cut.isin(['Fair','Good','Premium'])].shape


# In[66]:


# read only a subset of 3 rows from diamonds DataFrame

df1[1:4]


# In[69]:


# program to iterate through diamonds DataFrame

for index, row in df1.iterrows():
   print(index, row.carat, row.cut, row.color, row.price)


# In[71]:


#Include only numeric columns in the diamonds DataFrame

df1.select_dtypes(include=[np.number]).dtypes


# In[73]:


#pass a list of data types to only describe certain types of diamonds DataFrame

my_list = ['float','object']
df1.describe(include=my_list)


# In[77]:


# calculate the mean of each numeric column of diamonds DataFrame

df1.mean()


# In[78]:


# program to calculate the mean of each row of diamonds DataFrame

df1.mean(axis=1).head()


# In[80]:


# calculate the mean of price diamonds DataFrame
df1.price.mean()


# In[81]:


# # calculate the mean of price for each cut of diamonds DataFrame

df1.groupby('cut')['price'].mean()


# In[87]:


# program to calculate count, minimum, maximum price for each cut of diamonds DataFrame.

my_list = ['count','min','max']

df1.groupby('cut').price.agg(my_list)


# In[91]:


# program to count how many times each value in cut series of diamonds DataFrame occurs. 

(df1['cut'].value_counts())


# In[93]:


# program to display percentages of each value of cut series occurs in diamonds DataFrame.

df1['cut'].value_counts(normalize=True)


# In[94]:


# program to display the unique values in cut series of diamonds DataFrame

df1['cut'].unique()


# In[97]:


# program to count the number of unique values in cut series of diamonds DataFrame. 

df1.cut.nunique()


# In[98]:


df1.head(6)


# In[99]:


df1.shape


# In[102]:


# program to compute a cross-tabulation of two Series in diamonds DataFrame.

pd.crosstab(df1.cut,df1.color)


# In[103]:


# calculate various summary statistics of cut series of diamonds

df1['cut'].describe()


# In[104]:


df1['carat'].describe()


# In[106]:


# create a histogram of the 'carat' Series (distribution of a numerical variable) of diamonds DataFrame. 

df1['carat'].plot(kind = 'hist')


# In[109]:


# create a bar plot of the 'value_counts' for the 'cut' series of diamonds DataFrame. 

df1['cut'].value_counts().plot(kind = 'bar')


# In[111]:


# program to create a DataFrame of booleans (True if missing, False if not missing) from diamonds DataFrame.

df1.isnull().head(20)


# In[112]:


# rogram to count the number of missing values in each Series of diamonds DataFrame.

df1.isnull().sum()


# In[114]:


# program to check the number of rows and columns and drop those row if 'any' values are missing in a row of diamonds DataFrame. 

df1.dropna(how = 'any').shape


# In[115]:


# program to drop a row if any or all values in a row are missing of diamonds DataFrame 

df1.dropna(how = 'all').shape


# In[116]:


# program to set an existing column as the index of diamonds DataFrame

df1.set_index('color',inplace = True)
df1.head(6)


# In[117]:


# program to set an existing column as the index of diamonds DataFrame.
# restore the index name, and move the index back to a column

df1.reset_index('color',inplace=True)


# In[118]:


df1.head(6)


# In[119]:


# program to access a specified Series index and the Series values of diamonds DataFrame.

df1.columns


# In[121]:


df1['carat'].value_counts().index


# In[128]:


df1['cut'].value_counts().values


# In[129]:


# program to sort a Series by its values and index of diamonds DataFrame.


df1['cut'].value_counts().sort_values()


# In[127]:


df1['cut'].value_counts().sort_index()


# In[131]:


# program to calculate the multiply of length, width and depth for each cut of diamonds DataFrame. 

df2 = df1['x']*df1['y']*df1['z']


# In[132]:


df2.head(6)


# In[135]:


#program to concatenate the diamonds DataFrame with the 'color' Series. 

pd.concat([df1,df1['color']],axis = 1).head(6)


# In[138]:


# program to read specified rows and all columns of diamonds DataFrame

df1.loc[0, :]


# In[139]:


# program to read rows 0, 5, 7 and all columns of diamonds DataFrame

df1.loc[[0,5,7],:]


# In[141]:


# program to read rows 2 through 5 and all columns of diamonds DataFrame.

df1.loc[2:5,:]


# In[143]:


# program to read rows 0 through 2 (inclusive), columns 'color' and 'price' of diamonds DataFrame

df1.loc[0:2,['color','price']]


# In[145]:


# program to read rows 0 through 2 (inclusive), columns 'color' through 'price' (inclusive) of diamonds DataFrame

df1.loc[0:2,'color':'price']


# In[150]:


# Pandas program to read rows in which the 'cut' is 'Premium', column 'color' of diamonds DataFrame. 

df1.loc[df1['cut'] =='Premium','color'].head(6)


# In[154]:


# Pandas program to read rows in positions 0 and 1, columns in positions 0 and 3 of diamonds DataFrame. 

df1.iloc[[0,1],[0,3]]


# In[156]:


#Pandas program to read rows in positions 0 through 4, columns in positions 1 through 4 of diamonds DataFrame

df1.iloc[0:4,1:4]


# In[157]:


# program to read rows in positions 0 through 4 (exclusive) and all columns of diamonds DataFrame.

df.loc[0:3,:]


# In[159]:


# read rows 2 through 5 (inclusive), columns in positions 0 through 2 (exclusive) of diamonds DataFrame.

df1.iloc[2:5, 0:2]


# In[160]:


# program to print a concise summary of diamonds DataFrame

df1.info()


# In[162]:


# program to get the true memory usage by diamonds DataFrame

df1.info(memory_usage = 'deep')


# In[164]:


# program to calculate the memory usage for each Series (in bytes) of diamonds DataFrame

df1.memory_usage(deep = True)


# In[165]:


# program to get randomly sample rows from diamonds DataFrame

df1.sample(n=3)


# In[166]:


# to read the diamonds DataFrame and detect duplicate color

df1['clarity'].duplicated().sum()


# In[168]:


# program to count the duplicate rows of diamonds DataFrame

print(df1.duplicated().sum())


# In[ ]:




