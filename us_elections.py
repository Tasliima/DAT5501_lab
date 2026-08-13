import pandas as pd
import matplotlib.pyplot as plt

# Load election data
election_data = pd.read_csv('US-2016-primary.csv', delimiter=';')

# Select Donald Trump and John Kasich
trump = election_data[election_data['candidate'] == 'Donald Trump']
kasich = election_data[election_data['candidate'] == 'John Kasich']

# Plot histograms for both candidates
plt.hist(
    trump['fraction_votes'],
    bins=20,
    alpha=0.5,
    label='Donald Trump'
)

plt.hist(
    kasich['fraction_votes'],
    bins=20,
    alpha=0.5,
    label='John Kasich'
)

plt.xlabel('Fraction of Votes')
plt.ylabel('Number of Counties')
plt.title("Donald Trump vs John Kasich Vote Fractions")
plt.legend()

plt.show()