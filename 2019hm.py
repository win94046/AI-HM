
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[79]:


import math
N = 10000
d = 5
ads_selected = []
pi=[0.3,0.4,0.5,0.6,0.7]
numbers_of_selections = [0] * d
sums_of_reward = [0] * d
total_reward = 0


# In[80]:


for n in range(0, 10):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_reward[i] / numbers_of_selections[i]
            delta_i = math.sqrt(2 * math.log(n+1) / numbers_of_selections[i])
            upper_bound = pi[i] + delta_i
            #print(pi[i])
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
            
        if i ==0:
            reward = np.random.choice([-0.7,1],p=[0.7 , 0.3])
            sums_of_reward[ad] =sums_of_reward[ad]+ reward
            total_reward =total_reward+ reward
            print(reward,total_reward )
        if i ==1:
            reward = np.random.choice([-0.7,1],p=[0.6 , 0.4])
            sums_of_reward[ad] =sums_of_reward[ad]+ reward
            total_reward =total_reward+ reward  
            print(reward,total_reward )
        if i ==2:
            reward = np.random.choice([-0.7,1],p=[0.5 ,0.5])
            sums_of_reward[ad] =sums_of_reward[ad]+ reward
            total_reward =total_reward+ reward 
            print(reward,total_reward )
        if i ==3:
            reward = np.random.choice([-0.7,1],p=[0.4 , 0.6])
            sums_of_reward[ad] =sums_of_reward[ad]+ reward
            total_reward =total_reward+ reward 
            print(reward,total_reward )
        if i ==4:
            reward = np.random.choice([-0.7,1],p=[0.3 , 0.7])
            sums_of_reward[ad] =sums_of_reward[ad]+ reward
            total_reward =total_reward+ reward
            print(reward,total_reward )
    ads_selected.append(ad)
    numbers_of_selections[ad] += 1
print(total_reward)
    #reward = np.random.choice([-0.7,1],p=[1-pi[i], pi[i]])
    #sums_of_reward[ad] += reward
    #total_reward += reward


# In[78]:


print(pd.Series(ads_selected).head(10000).value_counts(normalize=True))


# In[51]:


p=[1-pi[0], pi[0]]


# In[52]:


p

