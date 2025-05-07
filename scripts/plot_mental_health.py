# scripts/plot_mental_health.py

import json
import matplotlib.pyplot as plt
from collections import Counter
import os

print("Plotting mental health intents...")

with open("data/mental_health.json", "r") as f:
    data = json.load(f)

# Correctly read "tag" instead of "intent"
labels = [item["tag"] for item in data.get("intents", []) if "tag" in item]
counts = Counter(labels)

print("Label counts:", counts)

plt.figure(figsize=(12, 6))
plt.bar(counts.keys(), counts.values(), color="skyblue")
plt.title("Mental Health Intents Distribution")
plt.xlabel("Intent")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.tight_layout()

os.makedirs("figures", exist_ok=True)
plt.savefig("figures/mental_health_plot.png")
print("Plot saved to: figures/mental_health_plot.png")
