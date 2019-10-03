#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from collections import Counter


# In[3]:


data=pd.read_csv('3_Full_Join_Cleaned.csv')
data.head()


# In[ ]:





# In[4]:


data.columns


# In[5]:


from sklearn.preprocessing import LabelEncoder
ToEncodeVars = ['feature_1','feature_5','feature_11','feature_23','feature_27','feature_32','feature_33',
                'feature_36','feature_37','feature_46','feature_48','feature_58',
                'feature_59','feature_60','feature_62','feature_72','feature_79']
enc=LabelEncoder()


# In[6]:


for i in ToEncodeVars:
    data[[i]] = enc.fit_transform(data[[i]])


# In[7]:


x=data.iloc[:,:-1]
x.head()


# In[8]:


data1 = data.drop('Bad_label',axis=1)
data1.head()


# In[9]:


y=data['Bad_label']


# In[10]:


x1=data1.iloc[:,:-1]
x1.head()


# In[11]:


y.head()


# In[12]:


from sklearn.model_selection import train_test_split
x_train, x_test ,y_train, y_test = train_test_split(x1,y,random_state = 10)


# # Random Forest

# In[13]:


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 100,random_state = 20)


# In[14]:


model.fit(x_train,y_train)


# In[15]:


x_train.head()

y_test.head()
# In[16]:


from sklearn.metrics import accuracy_score
y_predict  = model.predict(x_test)
print(accuracy_score(y_test,y_predict))


# In[ ]:





# In[17]:


importances = model.feature_importances_
print(importances)
indices = np.argsort(importances)
print(indices)
features = x.columns
print(features)


# In[18]:


from sklearn.metrics import confusion_matrix


# In[19]:


cm = confusion_matrix(y_test,y_predict)


# In[20]:


cm


# In[21]:


#LOGESTIC REGRESSION


# In[22]:


from sklearn.metrics import classification_report


# In[23]:


print(classification_report(y_test,y_predict))


# In[24]:


import matplotlib.pyplot as plt


# In[25]:


from sklearn.linear_model import LogisticRegression


# In[26]:


model = LogisticRegression()
model.fit(x_test,y_test)


# In[27]:


y_predict = model.predict(x_test)


# In[28]:


from sklearn.metrics import accuracy_score


# In[29]:


print(accuracy_score(y_test,y_predict))


# In[37]:


import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 10,20
plt.figure(1)
plt.title('Feature Importance')
plt.barh(range(len(indices)),importances[indices], color = 'b', align = 'center')
plt.yticks(range(len(indices)), features[indices])
plt.xlabel('Relative Importance')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




