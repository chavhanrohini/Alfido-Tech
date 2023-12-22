#!/usr/bin/env python
# coding: utf-8

# # 1. Import Libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


get_ipython().run_line_magic('ls', '')


# # 2. Load Uber Data

# In[21]:


uber_data = pd.read_csv('UberDataset.csv')


# # 3. Explore the Data

# In[113]:


uber_data


# In[114]:


# Display the first few rows of the DataFrame
print(uber_data.head())


# In[115]:


# Display the first few rows of the DataFrame
print(uber_data.head())


# In[116]:


# Check for missing values
print(uber_data.info())


# In[117]:


# Summary statistics
print(uber_data.describe())


# # 4. Time Analysis

# In[118]:


print(uber_data['START_DATE'])


# In[119]:


# Identify and remove the row with 'Totals'
uber_data = uber_data[uber_data['START_DATE'] != 'Totals']


# In[120]:


# Create a copy of the DataFrame
uber_data_copy = uber_data.copy()


# In[121]:


# Reattempt the conversion on the copied DataFrame
uber_data_copy['START_DATE'] = pd.to_datetime(uber_data_copy['START_DATE'], errors='coerce')


# In[122]:


# Verify the changes
print(uber_data_copy['START_DATE'])


# In[123]:


uber_data_copy


# In[124]:


# Replace the original DataFrame with the modified one
uber_data = uber_data_copy


# In[125]:


# Extract useful information from START_DATE
uber_data['hour'] = uber_data['START_DATE'].dt.hour
uber_data['day_of_week'] = uber_data['START_DATE'].dt.dayofweek


# In[126]:


uber_data['hour'] 


# In[127]:


# Visualize ride distribution over hours and days
plt.figure(figsize=(12, 6))
sns.countplot(x='hour', data=uber_data, palette='viridis')
plt.title('Uber Rides Distribution Over Hours')
plt.show()


# In[128]:


plt.figure(figsize=(12, 6))
sns.countplot(x='day_of_week', data=uber_data, palette='viridis')
plt.title('Uber Rides Distribution Over Days of the Week')
plt.show()


# # 5. Location Analysis

# In[129]:


print(uber_data.columns)


# In[130]:


import matplotlib.pyplot as plt
import seaborn as sns

# Assuming your DataFrame has columns 'START' and 'STOP'
pickup_locations = uber_data[['START', 'CATEGORY']].rename(columns={'START': 'Location', 'CATEGORY': 'Status'})
dropoff_locations = uber_data[['STOP', 'CATEGORY']].rename(columns={'STOP': 'Location', 'CATEGORY': 'Status'})


# In[131]:


# Concatenate the pickup and drop-off locations
all_locations = pd.concat([pickup_locations, dropoff_locations])


# In[132]:



# Count the occurrences of each location
location_counts = all_locations['Location'].value_counts()


# In[133]:


# Check the lengths of the 'Location' column and 'location_counts' variable
print(len(all_locations['Location']))
print(len(location_counts))


# In[134]:



# Merge the data
merged_data = pd.merge(all_locations, location_counts, left_on='Location', right_index=True)


# In[135]:


print(merged_data.columns)


# In[136]:


# Visualize pickup/drop-off locations using a bar plot
plt.figure(figsize=(15, 8))
sns.barplot(x=merged_data['Location_x'], y=merged_data['Location_y'], palette='coolwarm')
plt.title('Uber Pickup/Drop-off Locations')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()


# In[137]:


# Set the number of top locations to display
top_n = 50

# Get the top N locations
top_locations = merged_data['Location'].value_counts().head(top_n)

# Visualize pickup/drop-off locations using a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=top_locations.index, y=top_locations.values, palette='coolwarm')
plt.title(f'Top {top_n} Uber Pickup/Drop-off Locations')
plt.xlabel('Location')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()


# In[138]:


# Set the number of top locations to display in the pie chart
top_n = 15

# Get the top N locations
top_locations = merged_data['Location'].value_counts().head(top_n)

# Visualize pickup/drop-off locations using a pie chart
plt.figure(figsize=(8, 8))
plt.pie(top_locations, labels=top_locations.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('coolwarm'))
plt.title(f'Top {top_n} Uber Pickup/Drop-off Locations')
plt.show()


# # 6. Line Plot for Time Trends:

# In[139]:


import matplotlib.pyplot as plt
import seaborn as sns

#'hour' is the column representing the hour of the day
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='MILES', data=uber_data, estimator='sum', ci=None)
plt.title('Total Miles Over Hours of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Miles')
plt.show()


# # 7. Box Plot for Mileage Distribution:

# In[140]:


plt.figure(figsize=(12, 6))
sns.boxplot(x='PURPOSE', y='MILES', data=uber_data)
plt.title('Mileage Distribution by Purpose')
plt.xlabel('Purpose')
plt.ylabel('Miles')
plt.xticks(rotation=45, ha='right')
plt.show()


# # 8. Scatter Plot for Start and Stop Locations:

# In[141]:


plt.figure(figsize=(12, 8))
sns.scatterplot(x='START', y='STOP', hue='PURPOSE', data=uber_data)
plt.title('Scatter Plot of Start and Stop Locations')
plt.xlabel('Start Location')
plt.ylabel('Stop Location')
plt.show()


# # 9. Bar Plot for Day-of-Week Analysis:

# In[142]:


plt.figure(figsize=(10, 6))
sns.countplot(x='day_of_week', data=uber_data, palette='viridis')
plt.title('Number of Rides by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Rides')
plt.show()


# # 10. Heatmap for Hourly and Day-of-Week Patterns:

# In[143]:


heatmap_data = uber_data.groupby(['hour', 'day_of_week'])['MILES'].sum().unstack()

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt=".0f")
plt.title('Hourly and Day-of-Week Patterns')
plt.xlabel('Day of the Week')
plt.ylabel('Hour of the Day')
plt.show()


# # Barplot for Count of Rides for Each Purpose

# In[148]:


# Create a bar plot
plt.figure(figsize=(15, 8))
sns.countplot(x='Purpose', data=all_locations, palette='viridis')
plt.title('Count of Rides for Each Purpose')
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[ ]:





# In[146]:


print(all_locations.columns)


# # Barplot for hours for Each Purpose

# In[149]:


# Create a bar plot
plt.figure(figsize=(15, 8))
sns.countplot(x='Purpose', data=all_locations, palette='viridis')
plt.title('hours for Each Purpose')
plt.xlabel('Purpose')
plt.ylabel('hours')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[ ]:




