import numpy as np
def calculate_duration():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = np.datetime64('today')
    days = 365
    print("You have chosen:",start_date)
    print("The date today is:",end_date)
    start = np.datetime64(start_date, 'D')
    end = np.datetime64(end_date, 'D')
    duration = (end - start).astype(int)
    print("It has been:",duration, " days since", start_date)
    if duration > days:
        years = duration//days
        print("This is approximately", years, "years!")
    else:
        to_years = days - duration
        print ("This is", to_years, "away from a full year!")
calculate_duration()