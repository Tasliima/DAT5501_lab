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

# Calculate daily percentage change
data["Daily Change (%)"] = data["Close/Last"].pct_change() * 100

# Plot both graphs side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Closing price graph
ax1.plot(data["Date"], data["Close/Last"], color="blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Closing Price ($)")
ax1.set_title("NVIDIA Closing Price")
ax1.tick_params(axis="x", rotation=45)

# Daily percentage change graph
ax2.plot(data["Date"], data["Daily Change (%)"], color="green")
ax2.set_xlabel("Date")
ax2.set_ylabel("Daily Percentage Change (%)")
ax2.set_title("NVIDIA Daily Percentage Change")
ax2.tick_params(axis="x", rotation=45)

# Calculate standard deviation
standard_deviation = data["Daily Change (%)"].std()

# Add standard deviation as a text box
fig.text(
    0.5, 0.01,
    f"Standard deviation of daily percentage changes: {standard_deviation:.2f}%",
    ha="center",
    fontsize=11,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor="black")
)

plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.show()