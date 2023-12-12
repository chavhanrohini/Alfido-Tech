#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd

# Load data into a DataFrame
weather_data = pd.read_csv('C:/Users/Dell/weather_data.csv')

# Data cleaning
weather_data = weather_data.dropna()  # Drop rows with missing values
# Additional data cleaning steps...


# In[37]:


weather_data


# # Pairplot

# In[38]:


import seaborn as sns
import matplotlib.pyplot as plt

# EDA with Pandas
summary_stats = weather_data.describe()

# Visualization with Seaborn
sns.pairplot(weather_data[['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%','Wind Speed_km/h','Visibility_km', 'Press_kPa']])
plt.show()


# # Basic Statistics

# In[52]:


# Descriptive statistics
summary_stats = weather_data.describe()

# Correlation matrix
correlation_matrix = weather_data.corr()


# In[53]:


correlation_matrix


# # Visualization

# In[55]:


import matplotlib.pyplot as plt
import seaborn as sns

# Temperature trends over time
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date/Time'], weather_data['Temp_C'], label='Temperature (Celsius)')
plt.title('Temperature Trends Over Time')
plt.xlabel('Date/Time')
plt.ylabel('Temperature (Celsius)')
plt.legend()
plt.show()


# In[56]:


# Assuming the date information is in the 'Date/Time' column
# Convert the 'Date/Time' column to datetime format
if 'Date/Time' in weather_data.columns:
    weather_data_copy = weather_data.copy()

    # Convert the 'Date/Time' column to datetime format
    weather_data_copy['Date/Time'] = pd.to_datetime(weather_data_copy['Date/Time'])

    # Set the 'Date/Time' column as the index
    weather_data_copy.set_index('Date/Time', inplace=True)

    # Resample data to a specific frequency (e.g., monthly) for time series analysis
    monthly_data = weather_data_copy.resample('M').mean()
else:
    print("'Date/Time' column not found in the original DataFrame.")


# In[57]:


weather_data_copy


# In[43]:


import matplotlib.pyplot as plt

# Plotting mean temperature over months
plt.figure(figsize=(12, 6))
plt.plot(monthly_data.index, monthly_data['Temp_C'], marker='o', linestyle='-')
plt.title('Mean Temperature Over Months')
plt.xlabel('Month')
plt.ylabel('Mean Temperature (Celsius)')
plt.grid(True)
plt.show()


# # Line Chart for Multiple Variables:

# In[44]:


plt.figure(figsize=(12, 6))
plt.plot(monthly_data.index, monthly_data['Temp_C'], label='Temperature', marker='o', linestyle='-')
plt.plot(monthly_data.index, monthly_data['Wind Speed_km/h'], label='Wind Speed', marker='o', linestyle='-')
plt.title('Monthly Trends: Temperature vs Wind Speed')
plt.xlabel('Month')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()


# # Boxplot for Monthly Temperature Distribution:

# In[46]:


import seaborn as sns

plt.figure(figsize=(12, 6))
sns.boxplot(x=monthly_data.index.month, y=monthly_data['Temp_C'])
plt.title('Monthly Temperature Distribution')
plt.xlabel('Month')
plt.ylabel('Temperature (Celsius)')
plt.show()


# # Seasonal Decomposition:

# In[49]:


from statsmodels.tsa.seasonal import seasonal_decompose

# Assuming 'Temp_C' is the target variable
result = seasonal_decompose(monthly_data['Temp_C'], model='additive', period=6)
result.plot()
plt.suptitle('Seasonal Decomposition of Temperature')
plt.show()


# # Monthly variation of pressure

# In[58]:


import matplotlib.pyplot as plt

# Assuming 'Press_kPa' is the column representing pressure
plt.figure(figsize=(12, 6))
plt.plot(monthly_data.index, monthly_data['Press_kPa'], marker='o', linestyle='-')
plt.title('Monthly Variation of Pressure')
plt.xlabel('Month')
plt.ylabel('Pressure (kPa)')
plt.grid(True)
plt.show()


# In[60]:


import matplotlib.pyplot as plt

# Assuming 'Wind Speed_km/h' is the column representing wind speed
plt.figure(figsize=(12, 6))
plt.plot(monthly_data.index, monthly_data['Wind Speed_km/h'], marker='o', linestyle='-', label='Wind Speed')
plt.title('Monthly Variation of Wind Speed')
plt.xlabel('Month')
plt.ylabel('Wind Speed (km/h)')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




