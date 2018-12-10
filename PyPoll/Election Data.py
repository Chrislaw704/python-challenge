ls
# coding: utf-8

# In[ ]:


#Election data challenge
import os
import csv
import pandas as pd


#csvpath = os.path.join('..', 'Resources', 'accounting.csv')
csvpath = os.path.join('election_data.csv')
data_file = "election_data.csv"


# In[ ]:


data_file_pd = pd.read_csv(data_file)
data_file_pd.head()


# In[ ]:


#What does my data look like
data_file_pd.describe()


# In[ ]:


#Total number of votes
data_file_pd.count()


# In[ ]:


#List of Candidates that received votes
unique = data_file_pd["Candidate"].unique()
unique


# In[ ]:


#Total number of votes by candidate NOT WORKING
count = data_file_pd[unique].value_counts()
count


# In[ ]:


#Percentage of votes each candidate received


# In[ ]:


#Winner of election by vote

