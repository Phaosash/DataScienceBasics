import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#   This is used to display a corrlation matrix which is simply a table that shows
#   the correlation coefficients between variables
full_health_data = pd.read_csv("./Data/data.csv", header=0, sep=",")

#   round() is used to round the outputed values to only 2 decimal places.
Corr_Matrix = round(full_health_data.corr(), 2)

print(Corr_Matrix)

#   A heatmap is used to provide a visual representation of the correlation between
#   variables.
correlation_full_health = full_health_data.corr()

axis_corr = sns.heatmap(correlation_full_health, vmin = -1, vmax = 1, center = 0, cmap = sns.diverging_palette(50, 500, n = 500), square = True)

plt.show()