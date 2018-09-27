
# coding: utf-8

# In[57]:


import pandas as pd


# In[58]:


from matplotlib import pyplot as plt


# In[68]:


data = pd.read_csv('data.csv')


# In[67]:


plt.plot(data.age, data.population, "o")
plt.title("Ages in Lancaster")
plt.xlabel("Ages")
plt.ylabel("Population")
plt.legend(["Lancaster"])
plt.show()


# In[69]:


data

