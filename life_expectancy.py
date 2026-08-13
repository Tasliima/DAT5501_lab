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

# Forecast the final 10 years
x_test = testing["Year"].values
y_test = testing["Life expectancy"].values

forecasts = {}

for order, coefficients in models.items():
    predictions = np.polyval(coefficients, x_test)
    forecasts[order] = predictions

    print(f"Order {order} forecast:")
    print(predictions)

# Plot the actual data
plt.plot(
    x_train,
    y_train,
    label="Training data"
)

plt.plot(
    x_test,
    y_test,
    label="Actual 2014-2023"
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
plt.title("Polynomial Forecasts vs Actual Life Expectancy")
plt.legend()

plt.show()
