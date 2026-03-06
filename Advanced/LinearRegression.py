import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("./Data/data.csv", header = 0, sep = ",")

x = full_health_data["Average_Pulse"]
y = full_health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
 return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin = 0, ymax = 2000)
plt.xlim(xmin = 0, xmax = 200)
plt.xlabel("Average_Pulse")
plt.ylabel ("Calorie_Burnage")
plt.show()

'''
Linear Regression Explained:
    - Import the modules you need: Pandas, matplotlib and Scipy
    - Isolate Average_Pulse as x. Isolate Calorie_burnage as y
    - Get important key values with: slope, intercept, r, p, std_err = stats.linregress(x, y)
    - Create a function that uses the slope and intercept values to return a new value. This new value represents where on the y-axis the corresponding x value will be placed
    - Run each value of the x array through the function. This will result in a new array with new values for the y-axis: mymodel = list(map(myfunc, x))
    - Draw the original scatter plot: plt.scatter(x, y)
    - Draw the line of linear regression: plt.plot(x, mymodel)
    - Define maximum and minimum values of the axis
    - Label the axis: "Average_Pulse" and "Calorie_Burnage"
'''

#   This method is used to calculate the linear regression of the supplied value.
def Predict_Calorie_Burnage(Average_Pulse):
 return(0.3296 * Average_Pulse + 346.8662)
 
#Try some different values:
print(Predict_Calorie_Burnage(120))
print(Predict_Calorie_Burnage(130))
print(Predict_Calorie_Burnage(150))
print(Predict_Calorie_Burnage(180))