# --- IMPORT LIBRARIES ---
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
highlight = ["United Kingdom", "China", "India", "Germany"]
highlight_colors = ["tab:red", "tab:blue", "tab:purple", "tab:orange"]

years = sorted(merged["year"].unique())
width = 0.15  # width of each bar
fig, ax1 = plt.subplots(figsize=(14, 8))

# --- PLOT WORKING HOURS AS GROUPED BARS ---
for i, (country, color) in enumerate(zip(highlight, highlight_colors)):
    data = merged[merged["location_name"] == country].sort_values("year").dropna(subset=["Working Hours"])
    if data.empty:
        print(f"Warning: No working hours data for {country}")
        continue
    
    x_pos = np.arange(len(data))  # use data length in case some years are missing
    ax1.bar(x_pos + i*width, data["Working Hours"], width, label=f"{country} Hours", color=color, alpha=0.7)

ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Average Annual Working Hours per Worker", fontsize=12)
# Center x-ticks based on the number of years
ax1.set_xticks(np.arange(len(years)))
ax1.set_xticklabels(years)
ax1.grid(True, linestyle="--", alpha=0.3)

# --- PLOT NEUROLOGICAL DEATHS AS LINE ---
ax2 = ax1.twinx()
for i, (country, color) in enumerate(zip(highlight, highlight_colors)):
    data = merged[merged["location_name"] == country].sort_values("year").dropna(subset=["Neurological Deaths (thousands)"])
    if data.empty:
        print(f"Warning: No neurological deaths data for {country}")
        continue
    
    x_pos = np.arange(len(data))
    ax2.plot(x_pos + i*width, data["Neurological Deaths (thousands)"],
             color=color, marker="o", linestyle="-", linewidth=2, label=f"{country} Deaths")

ax2.set_ylabel("Neurological Disorder Deaths (thousands)", fontsize=12)

# --- COMBINE LEGENDS ---
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left", fontsize=10)

plt.title("Working Hours vs Neurological Deaths (2011-2019)", fontsize=16, weight="bold")
plt.tight_layout()
plt.savefig("working_hours_vs_neuro_deaths.png", dpi=300)
plt.show()


