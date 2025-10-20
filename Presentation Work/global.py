# --- IMPORT LIBRARIES ---
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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

# --- CONVERT NEUROLOGICAL DEATHS TO THOUSANDS ---
merged["Neurological Deaths (thousands)"] = merged["Neurological Deaths"] / 1000

# --- CHOOSE A RECENT YEAR FOR SNAPSHOT VIEW ---
latest_year = merged["year"].max()
snapshot = merged[merged["year"] == latest_year].dropna(subset=["Working Hours", "Neurological Deaths"])

# --- HIGHLIGHT SELECT COUNTRIES ---
highlight = ["United Kingdom", "China", "United States", "India", "Germany"]

plt.figure(figsize=(12, 8))

# Create a colormap for years
years = sorted(merged["year"].unique())
colors = cm.viridis((merged["year"] - min(years)) / (max(years) - min(years)))

# Plot all countries with colors according to year
plt.scatter(merged["Working Hours"], merged["Neurological Deaths (thousands)"],
            c=merged["year"], cmap="viridis", alpha=0.6, s=40, label="Countries by year")

# Highlight specific countries with lines over years
highlight_colors = ["tab:red", "tab:blue", "tab:green", "tab:purple", "tab:orange"]
for country, color in zip(highlight, highlight_colors):
    data = merged[merged["location_name"] == country].sort_values("year")
    if not data.empty:
        plt.plot(data["Working Hours"], data["Neurological Deaths (thousands)"],
                 color=color, marker="o", linewidth=2, label=country)
        for i, row in data.iterrows():
            plt.text(row["Working Hours"] + 5, row["Neurological Deaths (thousands)"] + 0.5,
                     f'{row["year"]}', fontsize=8, color=color)

# --- TITLES & LABELS ---
plt.title("Working Hours vs Neurological Deaths (2011-2019)", fontsize=16, weight="bold")
plt.xlabel("Average Annual Working Hours per Worker", fontsize=12)
plt.ylabel("Neurological Disorder Deaths (thousands)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.4)
plt.colorbar(label="Year")  # shows color mapping for years
plt.legend()
plt.tight_layout()
plt.show()