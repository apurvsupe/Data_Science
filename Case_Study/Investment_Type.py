# Given File 'startup_funding.csv'

# There are 4 different type of investments. Find out percentage of amount funded for each investment type.
# Plot a pie chart to visualise.
# Print the investment type and percentage of amount funded with 2 decimal places after rounding off.

# Note :
# Correct spelling of investment types are - "Private Equity", "Seed Funding", "Debt Funding", and "Crowd Funding". Keep an eye for any spelling mistake. You can find this by printing unique values from this column.
# Print the investment type in descending order with respect to the percentage of the amount funded.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

set = pd.read_csv("startup_funding.csv")

df = set.copy()
df['InvestmentType'].replace('PrivateEquity', 'Private Equity', inplace = True)
df['InvestmentType'].replace('SeedFunding', 'Seed Funding', inplace = True)
df['InvestmentType'].replace('Crowd funding', 'Crowd Funding', inplace = True)
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x : float(str(x).replace(',', '')))

type_funds = df.groupby(['InvestmentType'])['AmountInUSD'].sum().sort_values(ascending = False)[:10]
invest_type = type_funds.index
fundings = type_funds.values
percentage = np.true_divide(fundings, fundings.sum()) * 100

for i in range(len(invest_type)):
    
    print(invest_type[i], "%.2f"%percentage[i])

plt.pie(fundings, labels = invest_type, autopct = "%.2f%%")
plt.show()