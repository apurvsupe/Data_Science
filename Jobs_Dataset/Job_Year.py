# Plot the line graph between no. of Job postings with respect to year.
# Print the year and the number of job posting as integer value.
# Note: Year should be in ascending order.

import pandas as pd
import matplotlib.pyplot as plt

set = pd.read_csv("amazon_jobs_dataset.csv", encoding = 'utf-8')
date  = set['Posting_date']
year = date.str.split(', ', expand = True)[1]
freq = year.value_counts(ascending = True)
freq.sort_index(inplace = True, ascending = True)
x = freq.index
y = freq

for i in range(len(x)):
    print(x[i],y[i])

plt.plot(x, y)
plt.grid()
plt.xlabel('Year')
plt.ylabel('Number of Job Postings')
plt.show()