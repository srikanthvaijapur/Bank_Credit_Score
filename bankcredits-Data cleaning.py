#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


data = pd.read_csv('2_Full_Join_File.csv')
data.head()


# In[ ]:


data.columns


# In[ ]:


#Remove the irrelvant columns
data1=data.loc[:,['customer_no','feature_1', 'feature_4','feature_5','feature_6', 'feature_7','feature_11','feature_19','feature_23','feature_25', 'feature_26','feature_27','feature_29', 'feature_30', 'feature_31',
       'feature_32', 'feature_33', 'feature_34', 'feature_35','feature_36','feature_37' ,'feature_40', 'feature_41',
       'feature_42','feature_44' ,'feature_46','feature_48','feature_55','feature_56', 'feature_58', 'feature_59',
'feature_60','feature_62',  'feature_64',  'feature_66', 'feature_67', 'feature_68', 'feature_69',  'feature_71',
       'feature_72','feature_78','feature_78', 'feature_79', 'Bad_label','tot_high_credit_amt', 'tot_cur_balance_amt', 'total_amt_past_due',
       'tot_creditlimit', 'tot_cashlimit', 'enq_amt', 'total_enq_count']]


# In[ ]:


data1.head()


# In[ ]:





# In[ ]:


data1.head()


# In[ ]:


data1.replace(['?','*','$',' ','  ',''],np.nan,inplace=True)


# In[ ]:


data1.isnull().sum()


# In[ ]:


data1.loc[:,['feature_36','feature_27','feature_37','feature_46','feature_48']].info()


# In[ ]:



data1.loc[:,['feature_36','feature_27','feature_37','feature_46','feature_48']]=data1.loc[:,['feature_36','feature_27','feature_37','feature_46','feature_48']].replace(np.nan,'others')


# In[ ]:


data1.shape


# In[ ]:


from collections import Counter


# In[ ]:


from collections import Counter
Counter(data1.feature_36)


# In[ ]:


data1.shape


# In[ ]:


data1.drop_duplicates(inplace = True)
data1.shape


# In[ ]:


data1.isnull().sum()


# In[ ]:


data2=data1.loc[:,['customer_no','feature_1', 'feature_4','feature_5','feature_6', 'feature_7','feature_11','feature_19','feature_23','feature_25', 'feature_26','feature_27','feature_29', 'feature_30', 'feature_31',
       'feature_32', 'feature_33', 'feature_34', 'feature_35','feature_36','feature_37' ,'feature_40', 'feature_41',
       'feature_42','feature_44' ,'feature_46','feature_48','feature_55','feature_56', 'feature_58', 'feature_59',
'feature_60','feature_62',  'feature_64',  'feature_66', 'feature_67', 'feature_68', 'feature_69',  'feature_71',
       'feature_72', 'feature_78','feature_79','tot_high_credit_amt', 'tot_cur_balance_amt', 'total_amt_past_due',
       'tot_creditlimit', 'tot_cashlimit', 'enq_amt', 'total_enq_countt','Bad_label']]


# In[ ]:


data2.head()


# In[ ]:


data2.shape


# In[ ]:


data2.isnull().sum()


# In[ ]:


print(data2.shape)
data2.dropna(inplace = True)
print(data2.shape)


# In[ ]:


data2.isnull().sum()


# In[ ]:


data2.shape


# In[ ]:


data2.to_csv('D:bank details/4_Full_Join_Cleaned.csv',index = False)


# In[ ]:





# In[ ]:




