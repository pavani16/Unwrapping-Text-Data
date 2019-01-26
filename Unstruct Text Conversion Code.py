#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy

with open('htext.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '') 


# In[15]:


comma_data=data.split()
import pandas as pd

df= pd.DataFrame(comma_data)


# In[16]:


columns_df = df.iloc[6:17]
values_df=df.iloc[17:1117]
values_df.index


# In[17]:


row1_df=values_df.loc[17:27]
row1_df


# In[18]:


#columns_df.insert(loc=1,column='row1',value=[1,2,3,4,5,6,7,8,9,10,11])


# In[19]:


columns_df


# In[20]:


# single row creating chunks of 11 values and converting them to array type
row1_array_df = values_df.loc[17:27]
row1_array =row1_array_df.values


# In[21]:


row1_array


# In[22]:


#appending arrays to original data frame
columns_df.insert(loc=1,column='row1',value=row1_array)


# In[23]:


i=28
while i < 1100:
    columns_df.insert(loc=1,column=i,value=values_df.loc[i:i+10].values)
    i=i+11

columns_df


# In[24]:


output_df =columns_df.T


# In[25]:


import pandas as pd
output_df.to_csv('hspice_output.csv')

