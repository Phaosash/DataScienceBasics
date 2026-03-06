import pandas as pd
import numpy as np

full_health_data = pd.read_csv("./Data/data.csv", header=0, sep=",")
full_health_data.dropna()

#   Step 1: Calculating the mean
data_mean = np.mean(full_health_data)

print(data_mean)

#   Step 2: Find the difference from the mean
difference_from_mean = full_health_data - data_mean

print(difference_from_mean)

#   Step 3: Squaring each of the differences
squared_difference = difference_from_mean ** 2

print(squared_difference)

#   Step 4: Calculate the variance
data_variance = squared_difference.mean()

print(data_variance)