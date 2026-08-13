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

# Convert results to numpy arrays
n_values = np.array(n_values)
sorting_times = np.array(sorting_times)

# Calculate n log n
n_log_n = n_values * np.log(n_values)

# Scale n log n to match the measured sorting times
n_log_n_scaled = n_log_n * (sorting_times[-1] / n_log_n[-1])

# Plot measured sorting time
plt.plot(n_values, sorting_times, label="Measured sorting time")

# Plot n log n
plt.plot(n_values, n_log_n_scaled, label="n log n")

plt.xlabel("Number of elements (n)")
plt.ylabel("Sorting time (seconds)")
plt.title("Sorting Time vs n")
plt.legend()

# The measured sorting time broadly follows the shape of the n log n curve.
# However the measurements are a bit messy because the sorting operations are very fast.

plt.show()