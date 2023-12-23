#!/usr/bin/env python
# coding: utf-8

# # Load the Data:

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('ls', '')


# In[47]:


# Replace 'your_file.csv' with the actual file path
inventory_data = pd.read_csv('BegInvFINAL12312016.csv')


# # Explore the Data:

# In[48]:


inventory_data


# In[5]:


inventory_data.head


# In[49]:


inventory_data.columns


# In[6]:


print(inventory_data.info())


# In[7]:


print(inventory_data.describe())


# # Clean and Preprocess Data:

# # 1. Handling Missing Values

# In[8]:


# Check for missing values in each column
missing_values = inventory_data.isnull().sum()


# In[9]:


missing_values


# In[10]:


missing_values[missing_values > 0]


# # 2. Handling Duplicates:

# In[11]:


# Check for duplicates
duplicate_rows = inventory_data.duplicated()


# In[12]:


duplicate_rows


# In[13]:


# Display duplicate rows
print(inventory_data[duplicate_rows])


# # 3. Handling Outliers:

# In[15]:


# Use boxplots to visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=inventory_data['Brand'])
plt.title('Boxplot for Outlier Detection')
plt.show()


# In[16]:


# Use boxplots to visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=inventory_data['Price'])
plt.title('Boxplot for Outlier Detection')
plt.show()


# In[17]:


# Use boxplots to visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=inventory_data['onHand'])
plt.title('Boxplot for Outlier Detection')
plt.show()


# In[18]:


# Use boxplots to visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=inventory_data['Store'])
plt.title('Boxplot for Outlier Detection')
plt.show()


# # Remove Outliers (using IQR):

# In[19]:


# Calculate the Interquartile Range (IQR)
Q1 = inventory_data['Brand'].quantile(0.25)
Q3 = inventory_data['Brand'].quantile(0.75)
IQR = Q3 - Q1

# Define upper and lower bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


# In[20]:


# Remove outliers
inventory_data_no_outliers = inventory_data[(inventory_data['Brand'] >= lower_bound) & (inventory_data['Brand'] <= upper_bound)]


# In[21]:


inventory_data_no_outliers


# In[22]:


# Use boxplots to visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=inventory_data_no_outliers['Brand'])
plt.title('Boxplot for Outlier Detection')
plt.show()


# In[23]:


# Calculate the Interquartile Range (IQR)
Q4 = inventory_data['Price'].quantile(0.25)
Q5 = inventory_data['Price'].quantile(0.75)
IQR = Q5 - Q4

# Define upper and lower bounds
lower_bound = Q4 - 1.5 * IQR
upper_bound = Q5 + 1.5 * IQR


# In[24]:


# Remove outliers
inventory_data_no_outliers_price = inventory_data[(inventory_data['Price'] >= lower_bound) & (inventory_data['Price'] <= upper_bound)]


# In[25]:


# Use boxplots to visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=inventory_data_no_outliers_price['Price'])
plt.title('Boxplot for Outlier Detection')
plt.show()


# In[26]:


# Calculate the Interquartile Range (IQR)
Q6 = inventory_data['onHand'].quantile(0.25)
Q7 = inventory_data['onHand'].quantile(0.75)
IQR = Q7 - Q6

# Define upper and lower bounds
lower_bound = Q6 - 1.5 * IQR
upper_bound = Q7 + 1.5 * IQR


# In[27]:


# Remove outliers
inventory_data_no_outliers_onHand = inventory_data[(inventory_data['onHand'] >= lower_bound) & (inventory_data['onHand'] <= upper_bound)]


# In[28]:


# Use boxplots to visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=inventory_data_no_outliers_onHand['onHand'])
plt.title('Boxplot for Outlier Detection')
plt.show()


# In[29]:


# Calculate the Interquartile Range (IQR)
Q8 = inventory_data['Store'].quantile(0.25)
Q9 = inventory_data['Store'].quantile(0.75)
IQR = Q9 - Q8

# Define upper and lower bounds
lower_bound = Q8 - 1.5 * IQR
upper_bound = Q9 + 1.5 * IQR


# In[30]:


# Remove outliers
inventory_data_no_outliers_Store = inventory_data[(inventory_data['Store'] >= lower_bound) & (inventory_data['Store'] <= upper_bound)]


# In[31]:


# Use boxplots to visualize outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=inventory_data_no_outliers_Store['Store'])
plt.title('Boxplot for Outlier Detection')
plt.show()


# # Further Data Analysis and Visualization

# In[53]:


# Visualize the distribution of inventory levels
plt.figure(figsize=(20, 6))
sns.histplot(inventory_data['InventoryId'].sample(50), kde=True)  # Adjust the sample size as needed
plt.title('Inventory Distribution')
plt.show()


# # 1. Inventory Overview

# In[55]:


# Distribution of inventory across stores
plt.figure(figsize=(20, 6))
sns.countplot(x='Store', data=inventory_data)
plt.title('Inventory Distribution Across Stores')
plt.show()


# In[56]:



# Summary statistics for key variables
inventory_data[['onHand', 'Price']].describe()


# # 2. Store Analysis:

# In[58]:


# Analyze onHand quantity variations across stores
plt.figure(figsize=(20,6))
sns.barplot(x='Store', y='onHand', data=inventory_data, ci=None)
plt.title('Average onHand Quantity Across Stores')
plt.show()


# # 3. Brand Analysis:

# In[60]:


# Distribution of inventory across brands
plt.figure(figsize=(20,6))
sns.countplot(x='Brand', data=inventory_data)
plt.title('Inventory Distribution Across Brands')
plt.show()


# In[62]:


# Average price and onHand quantity for each brand
brand_stats = inventory_data.groupby('Brand').agg({'Price': 'mean', 'onHand': 'mean'})


# In[63]:


brand_stats


# # 4. Size Analysis

# In[67]:


# Distribution of inventory across sizes
plt.figure(figsize=(10,6))
sns.countplot(x='Size', data=inventory_data)
plt.title('Inventory Distribution Across Sizes')
plt.show()


# In[68]:


# Relationship between size and onHand quantity or price
plt.figure(figsize=(10,6))
sns.scatterplot(x='Size', y='onHand', data=inventory_data)
plt.title('Size vs onHand Quantity')
plt.show()


# # 5. Pricing Strategy

# In[70]:


# Relationship between price and onHand quantity
plt.figure(figsize=(20,6))
sns.scatterplot(x='Price', y='onHand', data=inventory_data)
plt.title('Price vs onHand Quantity')
plt.show()


# In[71]:


# Correlation between price changes and sales
inventory_data['Price'].corr(inventory_data['onHand'])


# # 6. Stockouts and Surpluses

# In[72]:


# Identify instances of stockouts
stockouts = inventory_data[inventory_data['onHand'] == 0]


# In[73]:


stockouts


# In[79]:


# Identify instances of surpluses
surpluses = inventory_data[inventory_data['onHand'] > 500]


# In[80]:


surpluses


# In[ ]:




