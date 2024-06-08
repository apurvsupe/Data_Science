# Plot the Bar graph between Month vs Job Openings.
# Print the month name and the number of job posting as integer value.
# Order of months doesn't matter.
    
# Open and read data file as specified in the question
# Print the required output in given format

import pandas as pd
import matplotlib.pyplot as plt

set = pd.read_csv("amazon_jobs_dataset.csv", encoding = "utf-8")
date = set['Posting_date']
month = date.str.split(expand = True)[0]
freq = month.value_counts(ascending = True)
month = freq.index
num_jobs = freq

for i in range(len(month)):
    
    print(month[i], num_jobs[i])

plt.xlabel('Month')
plt.ylabel('Number of Job Postings')
plt.bar(month, num_jobs)
plt.show()