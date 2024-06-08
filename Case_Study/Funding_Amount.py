# Given File 'startup_funding.csv'

# Find out if cities play any role in receiving funding.
# Find top 10 Indian cities with most amount of fundings received. Find out percentage of funding each city has got (among top 10 Indian cities only).
# Print the city and percentage with 2 decimal place after rounding off.

# Note:
# Take city name "Delhi" as "New Delhi".
# Check the case-sensitiveness of cities also. That means - at some place, instead of "Bangalore", "bangalore" is given. Take city name as "Bangalore".
# For few startups multiple locations are given, one Indian and one Foreign. Count those startups in Indian startup also. Indian city name is first.
# Print the city in descending order with respect to the percentage of funding.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('startup_funding.csv')
df=data.copy()
df['CityLocation'].dropna(inplace=True)

def seperatecity(city):
    return city.split('/')[0].strip()

df['CityLocation']=df['CityLocation'].apply(seperatecity)
df['CityLocation'].replace('Delhi','New Delhi',inplace=True)
df['CityLocation'].replace('banglore','Banglore',inplace=True)
df['AmountInUSD']=df['AmountInUSD'].apply(lambda x: float(str(x).replace(',', '')))
city_list=df.groupby(['CityLocation'])['AmountInUSD'].sum().sort_values(ascending=False)[0:10]

city=city_list.index
amount=city_list.values
percentage=np.true_divide(amount,amount.sum())*100

for x in range(len(city)):
    print(city[x],"%.2f"%percentage[x])
    
plt.pie(amount,labels=city,autopct='%.2f%%')
plt.show()