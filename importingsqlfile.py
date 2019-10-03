#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
import pandas as pd


# In[2]:


conn = create_engine('mysql+pymysql://dm_team1:dm_team1123#@18.136.56.185:3306/project_banking')


# In[3]:


conn


# In[12]:


Cust_accnt='select * from  Cust_Account'


# In[13]:


Cust_enq='select * from   Cust_Enquiry'


# In[14]:


Cust_DEmg = 'select * from Cust_Demographics'


# In[16]:


data123 = pd.read_sql(Cust_accnt,conn)


# In[17]:


data123.head()


# In[ ]:


data = pd.read_sql(query3,conn)


# In[ ]:


data.shape()


# In[ ]:


data.to_csv('D:bank details/Cust_Demographics.csv')


# In[ ]:


data.head()


# # ENQUIRY FILE TRANSFORM

# In[ ]:


x=pd.read_csv('Cust_Demographics')


# In[ ]:


x.head()


# In[ ]:





# In[ ]:




