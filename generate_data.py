import numpy as np
import pandas as pd

# Choose the original slope and intercept
m = 2
b = 5

# Generate X values
x = np.linspace(0, 10, 50)

# Generate Y values with some random noise
y = m * x + b + np.random.normal(0, 1, len(x))

# Save the data to a CSV file
data = pd.DataFrame({
    "x": x,
    "y": y
})

data.to_csv("synthetic_data.csv", index=False)

print("Synthetic data saved successfully.")
