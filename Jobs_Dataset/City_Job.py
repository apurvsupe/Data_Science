# Plot the Pie chart between Indian cities vs No. of job openings.
# Print the Indian cities and %age of Job distribution in India up to 2 decimal places.
# Note: %age of Job distribution should be in descending order.

# Open and read data file as specified in the question
# Print the required output in given format

import pandas as pd
import matplotlib.pyplot as plt

set = pd.read_csv("amazon_jobs_dataset.csv", encoding = "utf-8")

location = set['location']

country = location.str.split(', ', expand = True)[0]

city = location.str.split(', ', expand = True)[2]

j = 0

india_cities = pd.Series([])

for i in range(len(country)):
    
    # print(country[j])
    
    if country[i] == 'IN':
        
        india_cities[j] = city[i]
        
        # print(india_cities[j])
        # print(country[j])
        j += 1
        
freq = india_cities.value_counts(ascending = False)

# freq.sort_index(inplace = True, ascending = True)

india_cities = freq.index
num_jobs = freq
total_jobs = sum(num_jobs.values)
percentage_jobs = pd.Series([])

for i in range(len(num_jobs)):
    
    percentage_jobs[i] = ((num_jobs[i] / total_jobs) * 100)
    
    
for i in range(len(num_jobs)):
    
    print(india_cities[i], format(percentage_jobs[i], ".2f")) 
    
plt.pie(percentage_jobs, labels = india_cities, autopct = '%.2f', startangle = 90)
plt.axis('equal')
plt.show()