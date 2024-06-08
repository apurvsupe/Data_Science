# Given File 'startup_funding.csv'

# Check the trend of investments over the years. To check the trend, find -
# Total number of fundings done in each year.
# Plot a line graph between year and number of fundings. Take year on x-axis and number of fundings on y-axis.
# Print year-wise total number of fundings also. Print years in ascending order.
# Note :
# There is some error in the 'Date' feature. Make sure to handle that.

import pandas as pd
import matplotlib.pyplot as plt

set = pd.read_csv("startup_funding.csv", encoding = "utf-8")

date = set['Date']
year = date.str[-4:]
freq = year.value_counts(ascending = True)
freq.sort_index(inplace = True, ascending = True)
year = freq.index
fundings = freq

for i in range(len(year)):
    
    print(year[i], fundings[i])
    
plt.plot(year, fundings)
plt.xlabel('Year')
plt.ylabel('Number of fundings')
plt.show()