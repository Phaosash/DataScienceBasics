import pandas as pd
import statsmodels.formula.api as smf

#   Case: Use Duration + Average_Pulse to Predict Calorie_Burnage
full_health_data = pd.read_csv("./Data/data.csv", header=0, sep=",")

#   Create a Linear Regression Table with Average_Pulse and Duration as Explanatory Variables:
model = smf.ols('Calorie_Burnage ~ Average_Pulse + Duration', data = full_health_data)
results = model.fit()
print(results.summary())

'''
                                OLS Regression Results
    ==============================================================================
    Dep. Variable:        Calorie_Burnage   R-squared:                       0.816
    Model:                            OLS   Adj. R-squared:                  0.814
    Method:                 Least Squares   F-statistic:                     355.8
    Date:                Fri, 06 Mar 2026   Prob (F-statistic):           1.27e-59
    Time:                        13:57:59   Log-Likelihood:                -1007.7
    No. Observations:                 163   AIC:                             2021.
    Df Residuals:                     160   BIC:                             2031.
    Df Model:                           2
    Covariance Type:            nonrobust
    =================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
    ---------------------------------------------------------------------------------
    Intercept      -334.5194     73.616     -4.544      0.000    -479.904    -189.135
    Average_Pulse     3.1695      0.644      4.922      0.000       1.898       4.441
    Duration          5.8424      0.219     26.671      0.000       5.410       6.275
    ==============================================================================
    Omnibus:                      160.167   Durbin-Watson:                   2.339
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             5096.292
    Skew:                           3.383   Prob(JB):                         0.00
    Kurtosis:                      29.544   Cond. No.                     1.02e+03
    ==============================================================================

    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 1.02e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.

- Import the library statsmodels.formula.api as smf. Statsmodels is a statistical library in Python.
- Use the full_health_data set.
- Create a model based on Ordinary Least Squares with smf.ols(). Notice that the explanatory variable must be written first in the parenthesis. Use the full_health_data data set.
- By calling .fit(), you obtain the variable results. This holds a lot of information about the regression model.
- Call summary() to get the table with the results of linear regression.

The linear regression function can be rewritten mathematically as:
    Calorie_Burnage = Average_Pulse * 3.1695 + Duration * 5.8424 - 334.5194
Rounded to two decimals:
    Calorie_Burnage = Average_Pulse * 3.17 + Duration * 5.84 - 334.52
'''

#   Define the Linear Regression Function in Python
#   Define the linear regression function in Python to perform predictions.
def Predict_Calorie_Burnage(Average_Pulse, Duration):
 return(3.1695 * Average_Pulse + 5.8434 * Duration - 334.5194)

#   Average pulse is 110 and duration of the training session is 60 minutes = 365 Calories
print(Predict_Calorie_Burnage(110,60))

#   Average pulse is 140 and duration of the training session is 45 minutes = 372 Calories
print(Predict_Calorie_Burnage(140,45))

#   Average pulse is 175 and duration of the training session is 20 minutes = 337 Calories
print(Predict_Calorie_Burnage(175,20))

'''
Linear Regression Function Output (in call order):
    364.7296
    372.1636
    337.01110000000006
'''