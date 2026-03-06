import pandas as pd
import statsmodels.formula.api as smf

full_health_data = pd.read_csv("./Data/data.csv", header = 0, sep = ",")

model = smf.ols('Calorie_Burnage ~ Average_Pulse', data = full_health_data)
results = model.fit()
print(results.summary())

'''
Regression Table
The output from linear regression can be summarized in a regression table.

The content of the table includes:
    - Information about the model
    - Coefficients of the linear regression function
    - Regression statistics
    - Statistics of the coefficients from the linear regression function

                                OLS Regression Results
    ==============================================================================
    Dep. Variable:        Calorie_Burnage   R-squared:                       0.000
    Model:                            OLS   Adj. R-squared:                 -0.006
    Method:                 Least Squares   F-statistic:                   0.04975
    Date:                Fri, 06 Mar 2026   Prob (F-statistic):              0.824
    Time:                        13:37:58   Log-Likelihood:                -1145.8
    No. Observations:                 163   AIC:                             2296.
    Df Residuals:                     161   BIC:                             2302.
    Df Model:                           1
    Covariance Type:            nonrobust
    =================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
    ---------------------------------------------------------------------------------
    Intercept       346.8662    160.615      2.160      0.032      29.682     664.050
    Average_Pulse     0.3296      1.478      0.223      0.824      -2.588       3.247
    ==============================================================================
    Omnibus:                      124.542   Durbin-Watson:                   1.620
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):              938.541
    Skew:                           2.927   Prob(JB):                    1.58e-204
    Kurtosis:                      13.195   Cond. No.                         811.
    ==============================================================================

    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Example Explained:
    - Import the library statsmodels.formula.api as smf. Statsmodels is a statistical library in Python.
    - Use the full_health_data set.
    - Create a model based on Ordinary Least Squares with smf.ols(). Notice that the explanatory variable 
      must be written first in the parenthesis. Use the full_health_data data set.
    - By calling .fit(), you obtain the variable results. This holds a lot of information about the regression
      model.
    - Call summary() to get the table with the results of linear regression.
'''