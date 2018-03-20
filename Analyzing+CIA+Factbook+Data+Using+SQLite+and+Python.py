
# coding: utf-8

# In[5]:


import sqlite3
import pandas as pd
conn=sqlite3.connect("factbook.db")
cursor=conn.cursor()
q1="select * from sqlite_master WHERE type='table'";
pd.read_sql_query(q1,conn)


# In[6]:


q2="select * from facts LIMIT 5";
pd.read_sql_query(q2,conn)


# In[8]:


q3="select min(population) min_pop, max(population) max_pop, min(population_growth) min_pop_growth, max(population_growth) max_pop_growth from facts";
pd.read_sql_query(q3,conn)


# In[9]:


q4="select * from facts where population==(select min(population) from facts)";
pd.read_sql_query(q4,conn)


# In[10]:


q5="select * from facts where population==(select max(population) from facts)";
pd.read_sql_query(q5,conn)


# In[16]:


import matplotlib.pyplot as plt

import seaborn as sns
get_ipython().magic('matplotlib inline')

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(2,2,1)

q6 = '''
select population, population_growth, birth_rate, death_rate
from facts
where population != (select max(population) from facts)
and population != (select min(population) from facts);
'''
pd.read_sql_query(q6, conn).hist(ax=ax)


# In[23]:


q7 = "select cast(population as float)/cast(area as float) density from facts order by density desc limit 20"
pd.read_sql_query(q7, conn)
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(2,2,1)
pd.read_sql_query(q7, conn).hist(ax=ax)


# In[20]:


q7 = "select name, cast(population as float)/cast(area as float) density from facts order by density desc limit 20"
pd.read_sql_query(q7, conn)

