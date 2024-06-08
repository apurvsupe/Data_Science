# Given File 'startup_funding.csv'

# Which type of companies got more easily funding. To answer this question, find -
# Top 5 industries and percentage of the total amount funded to that industry. (among top 5 only)
# Print the industry name and percentage of the amount funded with 2 decimal place after rounding off.

# Note :
# Ecommerce is the right word in IndustryVertical, so correct it.
# Print the industry in descending order with respect to the percentage of the amount funded.

# Open and read data file as specified in the question
# Print the required output in given format

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = pd.read_csv("startup_funding.csv")
df = data.copy()
df['AmountInUSD'] = df['AmountInUSD'].apply(lambda x: float(str(x).replace(',', '')))
#df['IndustryVertical'].replace('eCommerce', 'ECommerce', inplace = True)
df['IndustryVertical'].replace('ECommerce','Ecommerce',inplace = True)
df['IndustryVertical'].replace('eCommerce','Ecommerce',inplace = True)
df['IndustryVertical'].replace('ecommerce','Ecommerce',inplace = True)

type_funds = df.groupby('IndustryVertical')['AmountInUSD'].sum().sort_values(ascending = False)[:5]
company_type = type_funds.index
funds = type_funds.values
percentage = np.true_divide(funds, funds.sum()) * 100

for i in range(len(company_type)):
    print(company_type[i], "%.2f"%percentage[i])