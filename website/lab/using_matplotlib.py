#!/usr/bin/env python
# coding: utf-8

# ### This tutorial shows how to use the matplotlib ( a Python package for visualization) to make a few basic plots

# ### Installing matplotlib

# #### Type the following command from the command line and hit enter

# In[89]:


pip install matplotlib


# #### If pip is not installed on your computer, follow this link
# ###### https://pip.pypa.io/en/stable/installation/

# #### Once matplotlib is installed, you will need to import it to make plots. Put the import command on top of your script

# In[81]:


# The name doesn't have to be plt. It is just convention
import matplotlib.pyplot as plt


# ### Scatter plot

# In[83]:


# Define two lists that will be used for the plots. List sizes have to be equal

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]

## To make a scatter plot

plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("This is a scatter plot")
plt.show()


# ### Simple line plot

# In[84]:


plt.plot(x,y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("This is a line plot")
plt.show()


# ### Putting both plots together

# In[85]:


## To make both on the same plot, just put them together
plt.scatter(x,y)
plt.plot(x,y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("This is a scatter plot on top of the line")
plt.show()


# ### Extra.... Some more parameters

# In[86]:


plt.figure(figsize=(5,5)) # To change figure size

# linewidth for width of the line, alpha to modify contrast, marker for marker style  
plot = plt.scatter(x,y,linewidths=2,alpha=0.7,marker="x")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Fine Tuned Plot')

plt.xlim(0,15) # Set limits on the X-axis
plt.ylim(0,125) # Set limit on the Y-axis
plt.savefig("demo_plot.png",dpi=800) # To save the plot on computer # increase dpi for better resolution


# ### To plot multiple lines using for loop on the same plot

# In[88]:


x = [1,2,3,4,5,6,7,8,9,10]
y1 = [1,2,3,4,5,6,7,8,9,10]
y2 = [1,4,9,16,25,36,49,64,81,100]
y3 = [y1,y2]

labels = ['linear','non linear']

for i in range(2):
    plt.plot(x,y3[i],label=labels[i],marker='o')
    
plt.legend() # To show the figure legend
plt.legend(bbox_to_anchor=(1, 0.95)) # To change the position of the legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple plots')
plt.show()

