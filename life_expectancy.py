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

# Fit a first-order polynomial (straight line)
x_train = training["Year"].values
y_train = training["Life expectancy"].values

coefficients = np.polyfit(x_train, y_train, 1)

print("Order 1 coefficients:", coefficients)
