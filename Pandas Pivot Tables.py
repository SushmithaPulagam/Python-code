#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df = pd.read_excel("C:\\Users\\VIAAN\\Desktop\\Kaggle Competitions\\SaleData.xlsx")


# In[2]:


df.head(6)


# In[26]:


# create a Pivot table with multiple indexes from a given excel sheet (Salesdata.xlsx).

df = pd.pivot_table(df,index = ['Region','SalesMan'])



# In[28]:


df.head(20)


# In[13]:


df1 = pd.read_excel("C:\\Users\\VIAAN\\Desktop\\Kaggle Competitions\\SaleData.xlsx")


# In[14]:


df1.head(6)


# In[15]:


df1.set_index('Region','SalesMan') 


# In[25]:


df1.groupby(['Region','SalesMan']).first()


# In[35]:


# program to create a Pivot table and find the total sale amount region wise, manager wise.  

df3 = pd.pivot_table(df1,index=['Region','Manager'],values = 'Sale_amt',aggfunc = 'mean')


# In[36]:


df3.head(10)


# In[41]:


# program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise

df4 = pd.pivot_table(df1,index=['Region','Manager','SalesMan'],values = 'Sale_amt',aggfunc = np.sum)


# In[43]:


df4.head(10)


# In[47]:


# Pandas program to create a Pivot table and find the item wise unit sold. 


df5 = pd.pivot_table(df1,index=['Item'],values = 'Units',aggfunc = np.sum)


# In[48]:


df5.head(6)


# In[49]:


# program to create a Pivot table and find the region wise total sale.

df6 = pd.pivot_table(df1, index=["Region"], values= 'Sale_amt', aggfunc = np.sum)



# In[50]:


df6.head(10)


# In[51]:


# program to create a Pivot table and find the region wise, item wise unit sold

df7 = pd.pivot_table(df1,index=['Region','Item'],values = 'Units', aggfunc = np.sum)


# In[52]:


df7.head(6)


# In[55]:


# program to create a Pivot table and count the manager wise sale and mean value of sale amount

df8 = pd.pivot_table(df1,index= ['Manager'],values = 'Sale_amt',aggfunc = [np.mean,len])


# In[56]:


df8.head(6)


# In[58]:


# Pandas program to create a Pivot table and find manager wise, 
# salesman wise total sale and also display the sum of all sale amount at the bottom.

df9 = pd.pivot_table(df1, index = ['Manager','SalesMan'],values = 'Sale_amt',aggfunc = np.sum,margins = True)


# In[60]:


df9


# In[65]:


# Pandas program to create a Pivot table and find the total sale amount region wise, 
# manager wise, sales man wise where Manager = "Douglas"

df10 = pd.pivot_table(df1,index=['Region','Manager','SalesMan'], values = 'Sale_amt')
print(df10.query('Manager == ["Douglas"]'))


# In[69]:


# Pandas program to create a Pivot table and find the region wise Television and Home Theater sold.

df11 = pd.pivot_table(df1, index= ['Region' ,'Item'],values = 'Units')
print(df11.query('Item == ["Television","Home Theater"]'))


# In[71]:


# program to create a Pivot table and find the maximum sale value of the items.

df12 = pd.pivot_table(df1,index = ['Item'], values = 'Sale_amt',aggfunc = np.max)


# In[72]:


df12.head(20)


# In[73]:


# Pandas program to create a Pivot table and find the minimum sale value of the items.

df13 = pd.pivot_table(df1,index = ['Item'], values = 'Sale_amt',aggfunc = np.min)
df13.head(20)


# In[74]:


td = pd.read_csv("C:\\Users\\VIAAN\\Desktop\\Kaggle Competitions\\Titanic\\titanic (1).csv")


# In[75]:


# program to print a concise summary of the dataset (titanic.csv). 
td.info()


# In[76]:


# program to extract the column labels, shape and data types of the dataset (titanic.csv). 

td.shape


# In[77]:


td.columns


# In[78]:


td.dtypes


# In[79]:


# program to create a Pivot table with multiple indexes from the data set of titanic.csv. 

td1 = pd.pivot_table(td,index=['sex','embarked'])


# In[80]:


td1.head(10)


# In[81]:


# \program to create a Pivot table and find survival rate by gender on various classes

td.columns


# In[83]:


td1 = pd.pivot_table(td, index = ['sex','class'], values = 'survived', aggfunc = np.sum)

td1.head(10)


# In[ ]:


# program to create a Pivot table and find survival rate by gender.

