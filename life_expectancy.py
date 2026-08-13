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

# Plot the full global life expectancy dataset
plt.figure(figsize=(12, 6))

plt.plot(
    world["Year"],
    world["Life expectancy"],
    marker="o",
    label="World life expectancy"
)

plt.xlabel("Year")
plt.ylabel("Life expectancy")
plt.title("Global Life Expectancy, 1770-2023")
plt.legend()

# Save the full historical plot
plt.savefig("global_life_expectancy.png")

plt.show()


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

# Calculate the sum of squared residuals for each model
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
# Plot the polynomial forecasts
plt.figure(figsize=(12, 6))

# Plot actual life expectancy
plt.plot(
    x_test,
    y_test,
    marker="o",
    label="Actual"
)

# Plot each polynomial forecast
for order, predictions in forecasts.items():
    plt.plot(
        x_test,
        predictions,
        label=f"Order {order}"
    )

plt.xlabel("Year")
plt.ylabel("Life expectancy")
plt.title("Polynomial Forecasts vs Actual Life Expectancy (2014-2023)")
plt.legend()

plt.show()
