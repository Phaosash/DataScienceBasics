import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("./Data/data.csv", header = 0, sep = ",")

health_data.dropna(axis = 0, inplace = True)

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line'),
plt.ylim(ymin=0, ymax=400)
plt.xlim(xmin=0, xmax=150)

plt.show()