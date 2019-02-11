#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x=np.arange(0,100)
y=x*2
z=x**2


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# Create a figure object called fig using plt.figure() 
# Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. 
# Plot (x,y) on that axes and set the labels and titles to match the plot below:

# In[4]:



fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.set_title('title')
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.plot(x,y)


# Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.

# In[5]:


fig1 = plt.figure()

ax1 = fig1.add_axes([0,0,1,1])
ax2 = fig1.add_axes([0.2,0.5,.2,.2])


# Now plot (x,y) on both axes. And call your figure object to show it

# In[6]:


fig1 = plt.figure()

ax1 = fig1.add_axes([0,0,1,1])
ax2 = fig1.add_axes([0.2,0.5,.2,.2])

ax1.plot(x,y)
ax2.plot(x,y)


# Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]

# In[7]:


fig1 = plt.figure()
ax0 = fig1.add_axes([0,0,1,1])
ax1 = fig1.add_axes([0.2,0.5,.4,.4])

ax0.set_xlabel('X')
ax0.set_ylabel('Z')

ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.set_ylim(30,50)
ax1.set_xlim(20,22)

ax0.plot(x,z)
ax1.plot(x,y)


# 
# Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:
# 

# In[8]:


fig1 = plt.figure()

ax3 = fig1.add_axes([0,0,1,1])
ax4 = fig1.add_axes([0.2,0.5,.4,.4])


# Use plt.subplots(nrows=1, ncols=2) to create the plot below.

# In[9]:



fig,axes = plt.subplots(nrows=1,ncols=2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




