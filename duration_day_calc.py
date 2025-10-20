import numpy as np
def calculate_duration():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = np.datetime64('today')
    print("You have chosen:",start_date)
    print("The date today is:",end_date)
    start = np.datetime64(start_date, 'D')
    end = np.datetime64(end_date, 'D')
    duration = (end - start).astype(int)
calculate_duration()