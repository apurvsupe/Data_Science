# Given File 'startup_funding.csv'

# Find out which cities are generally chosen for starting a startup.
# Find top 10 Indian cities which have most number of startups ?
# Plot a pie chart and visualise it.
# Print the city name and number of startups in that city also.

# Note :
# Take city name "Delhi" as "New Delhi".
# Check the case-sensitiveness of cities also. That means - at some place, instead of "Bangalore", "bangalore" is given. Take city name as "Bangalore".
# For few startups multiple locations are given, one Indian and one Foreign. Count those startups in Indian startup also. Indian city name is first.
# Print the city in descending order with respect to the number of startups.

# Open and read data file as specified in the question
# Print the required output in given format

import pandas as pd
import matplotlib.pyplot as plt

set = pd.read_csv("startup_funding.csv", encoding = "utf-8")

set['CityLocation'].dropna(inplace=True)
def sep(city):
    return city.split('/')[0].strip()
set['CityLocation']=set['CityLocation'].apply(sep)
set['CityLocation'].replace("Delhi","New Delhi",inplace=True)
set['CityLocation'].replace("bangalore","Bangalore",inplace=True)
cityn=set['CityLocation'].value_counts()[0:10]
city=cityn.index
numcity=cityn.values
for i in range(len(city)):
    print(city[i],numcity[i])