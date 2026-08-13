import pandas as pd
import matplotlib.pyplot as plt

# Load election data
election_data = pd.read_csv('US-2016-primary.csv', delimiter=';')

# Select Donald Trump's results
trump = election_data[election_data['candidate'] == 'Donald Trump']

# Create a histogram of Trump's fraction of votes
plt.hist(trump['fraction_votes'], bins=20)

plt.xlabel('Fraction of Votes')
plt.ylabel('Number of Counties')
plt.title("Donald Trump's Vote Fraction")

plt.show()