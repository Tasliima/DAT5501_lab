import pandas as pd
import numpy as np

#Load election data
election_data =pd.read_csv('US-2016-primary.csv',delimiter=';')
print(election_data.head())