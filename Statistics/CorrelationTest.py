import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

# Use 'Agg' if no interactive display is available
if not os.environ.get("DISPLAY"):
    matplotlib.use('Agg')

# Load your data
full_health_data = pd.read_csv("./Data/data.csv", header=0, sep=",")

# Create the plot
ax = full_health_data.plot(x='Duration', y='Max_Pulse', kind='scatter', title="Duration vs Max Pulse")

# Always save to a PNG
plt.savefig("chart.png")
print("Chart saved as chart.png")

# Try to show interactively (will work locally)
try:
    plt.show()
except Exception as e:
    print("Interactive display not available:", e)