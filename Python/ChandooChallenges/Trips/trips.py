# The goal of this challenge was to create a solution that
# finds all employees that went to two different locations. Specifically,
# the UK and USA. However, since those records were not provided. An example
# combination used was USA and Canada.

import pandas as pd

trips = pd.read_excel('Trips.xlsx')



result = (
    trips
    .groupby('Employee')['Country'].unique()
    .apply(lambda x: all(y in x for y in ['USA', 'Canada'])) 
    .loc[lambda x: x]
)

print(result)