import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the life expectancy data
data = pd.read_csv("life-expectancy.csv")

# Select global data
world = data[data["Entity"] == "World"]

# Use all data except the final 10 years for fitting
training = world[world["Year"] <= 2013]

# Keep the final 10 years to compare our forecasts with reality
testing = world[world["Year"] > 2013]

print("Training data:", training["Year"].min(), "to", training["Year"].max())
print("Testing data:", testing["Year"].min(), "to", testing["Year"].max())

# Prepare training data
x_train = training["Year"].values
y_train = training["Life expectancy"].values

# Fit polynomials from order 1 to 9
models = {}

for order in range(1, 10):
    coefficients = np.polyfit(x_train, y_train, order)
    models[order] = coefficients

    print(f"Order {order} coefficients:", coefficients)
