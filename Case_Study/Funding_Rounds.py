# Given File 'startup_funding.csv'

# Find the top 5 startups who received the most number of funding rounds. That means, startups which got fundings maximum number of times.
# Print the startup name in descending order with respect to the number of funding round as integer value.

# Note:
# Ola, Flipkart, Oyo, Paytm are important startups, so correct their names. There are many errors in startup names, ignore correcting all, just handle important ones.
# Open and read data file as specified in the question
# Print the required output in given format

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.read_csv("startup_funding.csv")
df = data.copy()
df['StartupName'].replace('Flipkart.com', 'Flipkart', inplace = True)
df['StartupName'].replace('Ola Cabs', 'Ola', inplace = True)
df['StartupName'].replace('Olacabs', 'Ola', inplace = True)
df['StartupName'].replace('Oyo Rooms', 'Oyo', inplace = True)
df['StartupName'].replace('OyoRooms', 'Oyo', inplace = True)
# df['StartupName'].replace('OYOfit', 'Oyo', inplace = True)
df['StartupName'].replace('Oyorooms', 'Oyo', inplace = True)
df['StartupName'].replace('OYO Rooms', 'Oyo', inplace = True)
df['StartupName'].replace('Paytm Marketplace', 'Paytm', inplace = True)
freq = df['StartupName'].value_counts(ascending = False)[:5]
startups = freq.index
num = freq.values 

for i in range(len(startups)):

    print(startups[i], num[i])