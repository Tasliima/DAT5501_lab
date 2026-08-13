import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("HistoricalData_1786643334520.csv")

# Convert the date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Remove $ signs and convert closing price to numbers
data["Close/Last"] = data["Close/Last"].str.replace("$", "").astype(float)

# Sort dates from oldest to newest
data = data.sort_values("Date")

# Plot closing price against date
plt.plot(data["Date"], data["Close/Last"])

plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.title("NVIDIA Closing Price Across One Year")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()