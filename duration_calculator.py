import numpy as np
def calculate_duration():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = np.datetime64('today')
    start = np.datetime64(start_date, 'D')
    end = np.datetime64(end_date, 'D')
    duration = (end - start).astype(int)
    return duration

calculate_duration()