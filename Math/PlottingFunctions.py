import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("./Data/data.csv", header = 0, sep = ",")

health_data.dropna(axis = 0, inplace = True)

print(health_data)

#   The plot() function is used to make a 2D hexagonal ninding plot of points on the x, y axis.
#   kind='line' is used to define that we want a striaght line to be used in this case.
health_data.plot(x = 'Average_Pulse', y = 'Calorie_Burnage', kind = 'line')

#   This defines what value we want the y axis to start on, in this case it starts at zero
plt.ylim(ymin = 0)

#   This defines what value we want the x axis to start on, in this case it starts at zero
plt.xlim(xmin = 0)

#   This shows the chart
plt.show()

#   This method is used to calculate the slope
def slope (x1, y1, x2, y2):
    s = (y2 - y1) / (x2 - x1)
    return s

print (slope(80, 240, 90, 260))