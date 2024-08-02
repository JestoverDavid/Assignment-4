#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Load the HR dataset
df_hr = pd.read_csv('HR_Dataset.csv')


# In[3]:


# Display the first few rows of the dataset
print(df_hr.head())


# In[4]:


# Check for missing values
print(df_hr.isnull().sum())


# In[5]:


# Handle missing values
# Fill missing 'ManagerID' with a placeholder (-1) indicating no manager
df_hr['ManagerID'].fillna(-1, inplace=True)


# In[6]:


# Fill missing 'LastPerformanceReview_Date' with a placeholder date
df_hr['LastPerformanceReview_Date'].fillna('No Review', inplace=True)


# In[7]:


# Check for duplicates and remove if any
df_hr.drop_duplicates(inplace=True)


# In[8]:


# Display dataset info and missing values
print(df_hr.info())


# In[9]:


# Display dataset info and missing values
print(df_hr.isnull().sum())


# In[10]:


# Install the required libraries
# !pip install matplotlib seaborn plotly altair

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt


# # 1. **Department Distribution (Bar Chart - matplotlib)**:
#    - **Column**: `Department`
#    - **Representation**: Bar chart (matplotlib)
#    - **Purpose**: To show the number of employees in each department.

# In[11]:


# Department Distribution - matplotlib
plt.figure(figsize=(10, 6))
sns.countplot(data=df_hr, x='Department')
plt.title('Department Distribution')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# # 2. **Gender Distribution (Pie Chart - matplotlib)**:
#    - **Column**: `Sex`
#    - **Representation**: Pie chart (matplotlib)
#    - **Purpose**: To visualize the gender distribution of employees.

# In[12]:


# Gender Distribution - matplotlib
plt.figure(figsize=(10, 6))
gender_distribution = df_hr['Sex'].value_counts()
gender_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()


# # 3. **Performance Scores Distribution (Bar Chart - seaborn)**:
#    - **Column**: `PerformanceScore`
#    - **Representation**: Bar chart (seaborn)
#    - **Purpose**: To show the distribution of performance scores among employees.

# In[13]:


# Performance Scores Distribution - seaborn
plt.figure(figsize=(10, 6))
sns.countplot(data=df_hr, x='PerformanceScore')
plt.title('Performance Scores Distribution')
plt.xlabel('Performance Score')
plt.ylabel('Count')
plt.show()


# # 4. **Salary Distribution (Histogram - seaborn)**:
#    - **Column**: `Salary`
#    - **Representation**: Histogram (seaborn)
#    - **Purpose**: To visualize the distribution of employee salaries.

# In[14]:


# Salary Distribution - seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df_hr, x='Salary', bins=30, kde=True)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()


# # 5. **Engagement Survey Scores (Histogram - seaborn)**:
#    - **Column**: `EngagementSurvey`
#    - **Representation**: Histogram (seaborn)
#    - **Purpose**: To show the distribution of engagement survey scores among employees.

# In[15]:


# Engagement Survey Scores - seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df_hr, x='EngagementSurvey', bins=30, kde=True)
plt.title('Engagement Survey Scores Distribution')
plt.xlabel('Engagement Survey Score')
plt.ylabel('Frequency')
plt.show()


# # 6. **Department Distribution (Bar Chart - plotly)**:
#    - **Column**: `Department`
#    - **Representation**: Bar chart (plotly)
#    - **Purpose**: To show the number of employees in each department.

# In[16]:


# Create the bar plot for department distribution
fig = px.bar(df_hr, x='DeptID', title='Department Distribution')
fig.show()


# # 7. **Gender Distribution (Pie Chart - altair)**:
#    - **Column**: `Sex`
#    - **Representation**: Pie chart (altair)
#    - **Purpose**: To visualize the gender distribution of employees.

# In[17]:


# Gender Distribution - altair
alt.Chart(df_hr).mark_arc().encode(
    theta=alt.Theta(field="Sex", type="nominal", stack=True),
    color=alt.Color(field="Sex", type="nominal")
).properties(
    title='Gender Distribution'
).show()


# # 8. **Performance Score vs. Salary (Scatter Plot - plotly)**:
#    - **Column**: `Salary`, `PerformanceScore`, `Department`
#    - **Representation**: Scatter plot (plotly)
#    - **Purpose**: To visualize the relationship between performance scores and salary.

# In[18]:


# Performance Score vs. Salary - plotly
fig = px.scatter(df_hr, x='Salary', y='PerformanceScore', color='Department', title='Performance Score vs. Salary')
fig.show()


# # 9. **Salary Distribution by Department (Box Plot - matplotlib)**:
#    - **Column**: `Salary`, `Department`
#    - **Representation**: Box plot (matplotlib)
#    - **Purpose**: To show the salary distribution across different departments.

# In[19]:


# Salary Distribution by Department - matplotlib
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_hr, x='Department', y='Salary')
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()


# # 10. **Engagement Survey vs. Performance Score (Scatter Plot - altair)**:
#    - **Column**: `EngagementSurvey`, `PerformanceScore`, `Department`
#    - **Representation**: Scatter plot (altair)
#    - **Purpose**: To visualize the relationship between engagement survey scores and performance scores.

# In[20]:


# Engagement Survey vs. Performance Score - altair
alt.Chart(df_hr).mark_circle(size=60).encode(
    x='EngagementSurvey',
    y='PerformanceScore',
    color='Department',
    tooltip=['EngagementSurvey', 'PerformanceScore', 'Department']
).properties(
    title='Engagement Survey vs. Performance Score'
).interactive()


# ## Submitted by Jestover Mark David (1206)
# 
