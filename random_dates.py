import numpy as np


def days_in_past(date):
    today = np.datetime64('today', 'D')
    date = np.datetime64(date, 'D')
    return (today - date).astype(int)


with open('random_dates.csv', 'r') as file:
    dates = file.read().splitlines()

for date in dates:
    days = days_in_past(date)
    print(f"The date {date} was {days} days ago.")