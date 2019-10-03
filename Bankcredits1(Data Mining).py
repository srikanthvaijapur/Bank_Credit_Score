#!/usr/bin/env python
# coding: utf-8
# DATA MINING
# In[1]:


from sqlalchemy import create_engine
import numpy as np
import pandas as pd


# # importing data 

# In[2]:


d1=pd.read_csv( 'Cust_Account.csv')
d1.head()


# In[3]:


d1.shape


# In[4]:


d2=pd.read_csv('Cust_Enquiry.csv')
d2.head()


# In[5]:


d3=pd.read_csv('Cust_Demographics.csv')
d3.head()


# In[6]:


d1.shape


# In[7]:


d2.shape


# In[8]:


d3.shape


# # ENQUIRY FILE TRANSFORM

# In[9]:


#Read and have a look at the data
d2=pd.read_csv('Cust_Enquiry.csv')
d2.head()


# In[10]:


d2.shape


# In[11]:


#Read list of columns
d2.columns


# In[12]:


## take only relevant colums in a new data frame
df1 = d2.loc[:,['customer_no','enq_amt']]
#df1[df1.customer_no == 1].count()
#df1_back==df1.copy()


# In[ ]:





# In[13]:


#group by operation
Cust_group = df1.groupby(['customer_no'])
print(Cust_group.sum().head())


# In[14]:


print(Cust_group.sum().shape)


# In[ ]:





# In[15]:


d2_amt = pd.DataFrame(Cust_group.sum()).reset_index()
d2_amt.columns = ['customer_no' , 'total_enq_amt']
print(d2_amt.head())
print(d2_amt.shape)


# In[16]:


df_count = pd.DataFrame(Cust_group.count()).reset_index()
df_count.columns = ['customer_no','total_enq_count']
print(df_count.head())
print(df_count.shape)


# In[17]:


#inner join
df_final = pd.merge(df_amt, df_count, on = 'customer_no', how='inner')
print(df_final.head())
print(df_final.shape


# In[18]:


df_final.to_csv('2_Cust_enquiry_Final.csv',index=False)


# # Account File Transformation

# In[19]:


d1.head()


# In[20]:


d1.columns


# In[21]:


ColList=['customer_no','high_credit_amt','cur_balance_amt','amt_past_due','creditlimit','cashlimit']
df1_a=d1.loc[:,ColList]
df1_a.head()


# In[22]:


df1_a.fillna(0,inplace=True)
df1_a.head()


# In[23]:


Cust_group_a = df1_a.groupby(['customer_no'])
#Cust_group_a.head()


# In[24]:


df_a_1 = pd.DataFrame(Cust_group_a.sum()).reset_index()
df_a_1.columns = ['customer_no','tot_high_credit_amt','tot_cur_balance_amt','total_amt_past_due','tot_creditlimit','tot_cashlimit']
print(df_a_1.head())
print(df_a_1.shape)


# In[25]:


df_a_1.to_csv('21_Cust_Account_Final.csv',index=False)


# # > JOINING THE DATA

# In[26]:


df_a = pd.read_csv('2_Cust_Account_Final.csv')


# In[27]:


df_e = pd.read_csv('2_Cust_enquiry_Final.csv')


# In[28]:


print(df_a.shape)
print(df_e.shape)
print(d3.shape)


# In[29]:


#left join with df_a
d3 = pd.merge(d3,df_a,on='customer_no',how='left')
d3.head()
d3.shape


# In[30]:


#left join with df_e
d3 = pd.merge(d3,df_e, on = 'customer_no',how = 'left')
d3.head()
d3.shape


# In[31]:


d3.to_csv('D:bank details/2_Full_Join_File.csv',index = False)


# In[32]:


d3.head()


# In[ ]:




