# --- IMPORT LIBRARIES ---
import pandas as pd
import matplotlib.pyplot as plt

# --- LOAD DATASETS ---
working_hours = pd.read_csv("annual-working-hours-per-worker.csv")
death_data = pd.read_csv("Global_Deaths.csv")

# --- FILTER NEUROLOGICAL DISORDERS FOR ALL COUNTRIES ---
neuro_data = death_data[
    (death_data["cause_name"] == "Neurological disorders") &
    (death_data["sex_name"] == "Both") &
    (death_data["age_name"] == "All ages")
][["location_name", "year", "val"]].rename(columns={"val": "Neurological Deaths"})

# --- RENAME & CLEAN WORKING HOURS DATA ---
hours_data = working_hours.rename(columns={
    "Entity": "location_name",
    "Year": "year",
    "Working hours per worker": "Working Hours"
})

# --- MERGE BOTH DATASETS ---
merged = pd.merge(hours_data, neuro_data, on=["location_name", "year"], how="inner")
merged["Neurological Deaths (thousands)"] = merged["Neurological Deaths"] / 1000

# --- HIGHLIGHT SELECT COUNTRIES ---
highlight = ["United Kingdom", "China", "United States", "India", "Germany"]
highlight_colors = ["tab:red", "tab:blue", "tab:green", "tab:purple", "tab:orange"]

plt.figure(figsize=(14, 8))

for country, color in zip(highlight, highlight_colors):
    data = merged[merged["location_name"] == country].sort_values("year")
    if not data.empty:
        # --- PLOT WORKING HOURS (LEFT Y-AXIS) ---
        plt.plot(data["year"], data["Working Hours"], color=color, marker="o", linestyle="-", label=f"{country} Hours")
        
# Create second y-axis for Neurological Deaths
ax1 = plt.gca()
ax2 = ax1.twinx()

for country, color in zip(highlight, highlight_colors):
    data = merged[merged["location_name"] == country].sort_values("year")
    if not data.empty:
        ax2.plot(data["year"], data["Neurological Deaths (thousands)"], color=color, marker="s", linestyle="--", label=f"{country} Deaths")

# --- TITLES & LABELS ---
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Average Annual Working Hours per Worker", fontsize=12)
ax2.set_ylabel("Neurological Disorder Deaths (thousands)", fontsize=12)
plt.title("Trends: Working Hours vs Neurological Deaths (2011-2019)", fontsize=16, weight="bold")
ax1.grid(True, linestyle="--", alpha=0.4)

# Combine legends from both axes
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
plt.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left", fontsize=10)

plt.tight_layout()
plt.show()
