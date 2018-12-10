#Pybank challenge
import os
import csv


#csvpath = os.path.join('..', 'Resources', 'accounting.csv')
csvpath = os.path.join('election_data.csv')

df_pd = pd.read_csv(data_file)
df_pd.head()