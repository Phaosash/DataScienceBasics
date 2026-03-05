import pandas as pd

#   Creates a data frame by reading the content of the data.csv file
#   header=0 means that the headers for the variable names are expected to
#   be found in the first row.
#   sep="," means that "," is used to seperate the values contained in the .csv file
health_data = pd.read_csv("data.csv", header=0, sep=",")

#   This prints out the entire contents of the data.csv file
print(health_data)

#   The .head() function call will result in only displaying the top 5 rows of data
print(health_data.head())

#   This removes any data rows that don't contain an actual number.
health_data.dropna(axis=0, inplace=True)

print(health_data)

#   The .info() function can be used to list all of the different data types within the data
print(health_data.info())

#   Converts the average pulse and max pulse into a float64 data type
health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print (health_data.info())

'''   
    The .describe() function can be used to summarise the data
    From the results:
        Count = Counts the number of observations
        Mean = the average value
        Std = the standard deviation
        Min = the lowest value
        25%, 50% and 75% = percentiles
        Max = the highest value
'''
print(health_data.describe())