# scripts/plot_air_quality.py

import pandas as pd
import matplotlib.pyplot as plt

print("Plotting air quality trends...")

df = pd.read_csv("data/air_quality_clean.csv", parse_dates=["date"])

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["no2"], label="NO2")
plt.plot(df["date"], df["o3"], label="O3")
plt.plot(df["date"], df["so2"], label="SO2")
plt.plot(df["date"], df["co"], label="CO")
plt.xlabel("Date")
plt.ylabel("Pollutant Level (ppm)")
plt.title("Air Quality Trends Over Time")
plt.legend()
plt.tight_layout()
plt.savefig("figures/air_quality_trends.png")
print("Plot saved to: figures/air_quality_trends.png")
