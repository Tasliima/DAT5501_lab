import pandas as pd
import numpy as np
import matplotlib as plt

# Load election data
election_data =pd.read_csv('US-2016-primary.csv',delimiter=';')
print(election_data.head())

# Create a histogram of the votes for each candidate by state
election_data.hist(column='Votes', by='State', figsize=(15.10), bins=20)
plt.plot.show()