import pandas as pd
import matplotlib.pyplot as plt

# Load the life expectancy data
data = pd.read_csv("life-expectancy.csv")

# Select global data
world = data[data["Entity"] == "World"]

# Plot global life expectancy
plt.plot(world["Year"], world["Life expectancy"])

plt.xlabel("Year")
plt.ylabel("Life expectancy")
plt.title("Global Life Expectancy Over Time")

plt.show()
