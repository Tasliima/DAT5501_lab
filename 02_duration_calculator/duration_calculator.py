import numpy as np


def calculate_duration(start_date):
    end_date = np.datetime64('today', 'D')
    start = np.datetime64(start_date, 'D')
    duration = (end_date - start).astype(int)
    return duration


if __name__ == "__main__":
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    print(calculate_duration(start_date))