import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the life expectancy data
data = pd.read_csv("life-expectancy.csv")

# Select global data
world = data[data["Entity"] == "World"]

# Split the data into training and testing sets
# The final 10 years are kept for testing
training = world[world["Year"] <= 2013]
testing = world[world["Year"] > 2013]

print("Training data:", training["Year"].min(), "to", training["Year"].max())
print("Testing data:", testing["Year"].min(), "to", testing["Year"].max())

# Prepare training data
x_train = training["Year"].values
y_train = training["Life expectancy"].values

# Fit polynomial models from order 1 to 9
models = {}

for order in range(1, 10):
    coefficients = np.polyfit(x_train, y_train, order)
    models[order] = coefficients

    print(f"Order {order} coefficients:", coefficients)

# Prepare testing data
x_test = testing["Year"].values
y_test = testing["Life expectancy"].values

# Forecast the final 10 years
forecasts = {}

for order, coefficients in models.items():
    predictions = np.polyval(coefficients, x_test)
    forecasts[order] = predictions

    print(f"Order {order} forecast:")
    print(predictions)

# Calculate chi-squared for each model
chi_squared = {}

for order, predictions in forecasts.items():
    residuals = y_test - predictions
    chi_squared[order] = np.sum(residuals ** 2)

    print(f"Order {order} chi-squared:", chi_squared[order])

# Calculate chi-squared per degree of freedom
chi_squared_reduced = {}

for order, chi_value in chi_squared.items():
    degrees_of_freedom = len(y_test) - (order + 1)

    if degrees_of_freedom > 0:
        reduced_chi_squared = chi_value / degrees_of_freedom
    else:
        reduced_chi_squared = np.nan

    chi_squared_reduced[order] = reduced_chi_squared

    print(
        f"Order {order} chi-squared per degree of freedom:",
        reduced_chi_squared
    )

# Create two graphs side by side
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Left graph: full historical data
axes[0].plot(
    world["Year"],
    world["Life expectancy"],
    marker="o",
    label="World life expectancy"
)

axes[0].set_xlabel("Year")
axes[0].set_ylabel("Life expectancy")
axes[0].set_title("Global Life Expectancy, 1770-2023")
axes[0].legend()

# Right graph: polynomial forecasts
axes[1].plot(
    x_test,
    y_test,
    marker="o",
    label="Actual"
)

for order, predictions in forecasts.items():
    axes[1].plot(
        x_test,
        predictions,
        label=f"Order {order}"
    )

axes[1].set_xlabel("Year")
axes[1].set_ylabel("Life expectancy")
axes[1].set_title("Polynomial Forecasts vs Actual")
axes[1].legend()

plt.tight_layout()

# Save the combined figure
plt.savefig("life_expectancy_forecasts.png")

plt.show()
