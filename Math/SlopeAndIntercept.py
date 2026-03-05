import pandas as pd
import numpy as np

#   This loads the data
health_data = pd.read_csv("./Data/data.csv", header = 0, sep = ",")

health_data.dropna(axis=0, inplace=True)

'''
    This is used to safely convert the columns to numeric safely.
    Original code line that was causing errors: x = health_data["Average_Pulse"]
    As despite this being as written in the tutorial it was causing issues as it wasn't
    reading the "Average_Pulse" as a float, but rather as a string.
    
    errors='coerce' is used to tell pandas that if a value cannot be converted to a number, then replace
    that value with NaN instead of throwing an error
'''
x = pd.to_numeric(health_data["Average_Pulse"], errors='coerce')
y = pd.to_numeric(health_data["Calorie_Burnage"], errors='coerce')

#   This is used to remove the rows where the conversion fails
mask = ~np.isnan(x) & ~np.isnan(y)
x = x[mask]
y = y[mask]

#   This is used to calculate the slope and intercept
#   The 1 in this method reperesents the degree in the linear function
#   which means that all coefficients are in the power of 1.
slope_intercept = np.polyfit(x, y, 1)

print(f"Slope and Intercept = {slope_intercept}")

#   Alternative approach to handling the function
def my_function (x):
    return 2 * x + 80

print (my_function(140))