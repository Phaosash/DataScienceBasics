import pandas as pd
import numpy as np

full_health_data = pd.read_csv("./Data/data.csv", header=0, sep=",")

Max_Pulse= full_health_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)

print(percentile10)

#   Standard Deviation
std = np.std(full_health_data)

print(std)

#   Coefficient of variation
cv = np.std(full_health_data) / np.mean(full_health_data)

print(cv)

#   Variance
var = np.var(full_health_data)
print(var)