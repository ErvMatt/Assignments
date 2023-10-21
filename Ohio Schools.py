#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import pandas as pd


# In[ ]:


# The data to follow includes Ohio's year-end test results for all 606 school districts. 
# Although there are a number of IVs and DVs in this data set, for this exercise the focus is 
# on the following, IV = Federal Average Income for TY 2020 and 
# DVs = The Percent of Students Advanced ACC+ADV +Plus(Students testing above Proficient) 

# Mean: #
# Federal Average Income TY20                           65,335 
# Percent of Students Advanced ACC+ADV +Plus             37.57% 

# Median: 
# Federal Average Income TY20                           57,942 
# Percent of Students Advanced ACC+ADV +Plus               35.95% 

# Minimum:
# Federal Average Income TY20                             29,716 
# Percent of Students Advanced ACC+ADV +Plus                  3.80% 

# Maximum: 
# Federal Average Income TY20                               481,096 
# Percent of Students Advanced ACC+ADV +Plus                  77.9% 

# The Scatter Plot Clearly Shows the Relationship of Income and Higher Academic Achievement 
# Districts with higher Average Incomes also have higher Academic scores and Districts with 
# lower Average Incomes have considerably lower Academic scores. For example, the lowest-scoring 
# district, East Cleveland, also has the lowest average income, $29,716. Conversely, 
# the highest-scoring district, Solon City, has an average income of $131,695 


# In[40]:


df = pd.read_excel(r"C:\Users\Win_10\Documents\Ohio Data\FY22Ohio_P.xlsx")
df


# In[44]:


mean = data["Federal Average Income TY20"].mean()
print("Mean:", mean)
mean = data.mean()
median = data.median()
minimum = data.min()
maximum = data.max()
mode = data.max()

print('Mean:', mean)

print('Median:', median)

print('Minimum:', minimum)

print('Maximum:', maximum)

print('Mode', mode)


# In[51]:


import matplotlib.pyplot as plt
import pandas as pd

# File Path
file_path = "C:\\Users\\Win_10\\Documents\\Ohio Data\\FY22Ohio_P.xlsx"

# Read data from the Excel file into a Pandas DataFrame
data = pd.read_excel(file_path)

# Extract columns 
income_ty20 = data['Federal Average Income TY20']
percent_advanced = data['Percent of Students Advanced ACC+ADV +Plus']

# Scatter plot
plt.scatter(income_ty20, percent_advanced)

# Labels
plt.xlabel('Federal Average Income TY20')
plt.ylabel('Percent of Students Advanced ACC+ADV+Plus')

# Graph title
plt.title('Scatter Plot: Federal Average Income TY20 vs Percent Advanced Students')

# Show the plot
plt.show()

