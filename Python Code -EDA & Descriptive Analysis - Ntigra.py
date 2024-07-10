#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd

# Load the dataset

data = pd.read_excel(r"D:\Copy of SampleData (003).xlsx")

# Display the first few rows of the dataset to understand its structure and contents
data.head()


# In[16]:


# Check for missing values in the dataset
missing_values = data.isnull().sum()

# Summary of missing values
missing_values


# # Data Cleaning Insights
# DenialCode and DenialDescription have a large number of missing values (28,036 out of the total rows). These missing values likely correspond to claims that were not denied.

# # Steps for Data Cleaning
# 

# # 1. Handling Missing Values:
# 
# For DenialCode and DenialDescription, fill missing values with "Not Denied" to indicate that these claims were approved.

# In[17]:


# Fill missing values for DenialCode and DenialDescription with "Not Denied"
data['DenialCode'].fillna('Not Denied', inplace=True)
data['DenialDescription'].fillna('Not Denied', inplace=True)


# In[18]:


# Check for missing values in the dataset
missing_values = data.isnull().sum()

# Summary of missing values
missing_values


# # 2. Data Type Checks:
# 
# Ensure that numerical columns (Quantity, ClaimedAmount, PaidAmount) are in the correct format.

# In[19]:


# Check data types
data.dtypes


# # 3. Generate Additional Insights:
# 
# Create a new column indicating whether a claim was denied or approved.

# In[20]:


# Create a new column to indicate if a claim was denied
data['ClaimStatus'] = data['DenialCode'].apply(lambda x: 'Denied' if x != 'Not Denied' else 'Approved')


# In[21]:


data.head()


# # Descriptive Statistics:
# 
# 1. Calculate basic statistics for ClaimedAmount and PaidAmount.
# 2. Count of denied vs approved claims.

# In[22]:


# Calculate basic statistics for ClaimedAmount and PaidAmount
claimed_amount_stats = data['ClaimedAmount'].describe()
paid_amount_stats = data['PaidAmount'].describe()

# Count of denied vs approved claims
claim_status_counts = data['ClaimStatus'].value_counts()

claimed_amount_stats, paid_amount_stats, claim_status_counts


# # The provided data represents summary statistics and count data for a dataset containing information on insurance claims. 
# Here’s a breakdown of each part:

# # ClaimedAmount
# 1) count: 35,923 claims have a recorded claimed amount.
# 2) mean: The average claimed amount is 166.40.
# 3) std (standard deviation): The claimed amounts vary by an average of 1178.79 from the mean.
# 4) min: The minimum claimed amount is 0.
# 5) 25% (first quartile): 25% of claims have an amount of 0, meaning a quarter of the claims are 0.
# 6) 50% (median): 50% of claims have an amount of 8, meaning half of the claims are 8 or less.
# 7) 75% (third quartile): 75% of claims have an amount of 60, meaning three-quarters of the claims are 60 or less.
# 8) max: The maximum claimed amount is 68,000.

# # PaidAmount
# 1) count: 35,923 claims have a recorded paid amount.
# 2) mean: The average paid amount is 146.72.
# 3) std (standard deviation): The paid amounts vary by an average of 1155.88 from the mean.
# 4) min: The minimum paid amount is -180. This could indicate a refund or overpayment adjustment.
# 5) 25% (first quartile): 25% of claims have a paid amount of 0, meaning a quarter of the claims are not paid.
# 6) 50% (median): 50% of claims have a paid amount of 0, meaning half of the claims are not paid.
# 7) 75% (third quartile): 75% of claims have a paid amount of 37.50, meaning three-quarters of the claims are 37.50 or less.
# 8) max: The maximum paid amount is 61,116.28.

# # ClaimStatus
# 1) Approved: 28,036 claims have been approved.
# 2) Denied: 7,887 claims have been denied.

# # Summary
# 1) The majority of the claimed amounts are low, with a median of 8 and a high standard deviation, indicating a few high-value claims skewing the average.
# 
# 2) Similarly, the paid amounts also show a low median of 0, suggesting many claims are not paid, and a few high-value payments increase the average.
# 
# 3) There are more approved claims (28,036) than denied ones (7,887), indicating a higher approval rate for the claims.

# In[29]:


# writing the final dataframe to an excel file that we will use in our Power BI visualisations.
#The file will be the 'SampleData(003)_final.xlsx' file and the sheet name is 'Data'
data.to_excel('SampleData(003)_final.xlsx', sheet_name='Data')


# In[ ]:





# In[ ]:




