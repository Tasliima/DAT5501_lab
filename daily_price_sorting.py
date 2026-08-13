import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Load the asset price data
data = pd.read_csv("HistoricalData_1786643334520.csv")

# Clean the Close/Last column
data["Close/Last"] = data["Close/Last"].replace(r"[$,]", "", regex=True).astype(float)

# Calculate daily price changes
prices = data["Close/Last"].values
price_changes = prices[:-1] - prices[1:]

# Store sorting times
n_values = []
sorting_times = []

# Test different data sizes from 7 to 365
for n in range(7, min(366, len(price_changes) + 1)):

    values = price_changes[:n].copy()

    start_time = time.perf_counter()

    np.sort(values)

    end_time = time.perf_counter()

    sorting_time = end_time - start_time

    n_values.append(n)
    sorting_times.append(sorting_time)

# Calculate daily price changes
prices = data["Close/Last"].values
price_changes = prices[:-1] - prices[1:]

print(price_changes[:10])

# Plot sorting time against n
plt.plot(n_values, sorting_times)

plt.xlabel("Number of elements (n)")
plt.ylabel("Sorting time (seconds)")
plt.title("Sorting Time vs Number of Price Changes")

plt.show()

# Store the number of elements and sorting times
n_values = []
sorting_times = []

# Test sorting times for different values of n
for n in range(7, min(366, len(price_changes) + 1)):

    # Select the first n price changes
    values = price_changes[:n].copy()

    # Start timer
    start_time = time.perf_counter()

    # Sort the price changes
    np.sort(values)

    # Stop timer
    end_time = time.perf_counter()

    # Calculate elapsed time
    sorting_time = end_time - start_time

    # Store results
    n_values.append(n)
    sorting_times.append(sorting_time)

print("Number of tests:", len(n_values))
print("First sorting time:", sorting_times[0])
print("Last sorting time:", sorting_times[-1])