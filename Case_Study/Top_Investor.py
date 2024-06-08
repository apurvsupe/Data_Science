# Given File 'startup_funding.csv'

# Find the Investors who have invested maximum number of times.
# Print the investor name and number of times invested as integer value.

# Note:
# In startup, multiple investors might have invested. So consider each investor for that startup.
# Ignore the undisclosed investors.

import pandas as pd
import numpy as np

df = pd.read_csv('startup_funding.csv',encoding = 'utf-8')
df['InvestorsName'].dropna(inplace = True)

def createDict(array):
    dictionary = {}
    for i in array:
        if ',' not in i:
                dictionary[i] = dictionary.get(i,0)+1
                
        else:
            string = i.strip().split(',')
            for j in string:
                dictionary[i]=dictionary.get(j,0)+1
    return dictionary

dictionary = createDict(df['InvestorsName'])
dataf = pd.DataFrame(list(dictionary.values()),list(dictionary.keys()))
dataf = dataf.sort_values(by = [0], ascending = False)
print(dataf.index[0],dataf.values[0][0])