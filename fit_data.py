import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the synthetic data
data = pd.read_csv("synthetic_data.csv")

x = data["x"]
y = data["y"]

# Fit a straight line
m_fit, b_fit = np.polyfit(x, y, 1)

print("Measured slope:", m_fit)
print("Measured intercept:", b_fit)

# Original line
y_original = 2 * x + 5

# Best-fit line
y_fit = m_fit * x + b_fit

# Plot the data and both lines
plt.scatter(x, y, label="Synthetic data")
plt.plot(x, y_original, label="Original line")
plt.plot(x, y_fit, label="Best-fit line")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Synthetic Data and Best-Fit Line")
plt.legend()

plt.savefig("synthetic_data_plot.png")
plt.show()
