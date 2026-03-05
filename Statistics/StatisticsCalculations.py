import numpy as np
import pandas as pd

class Calculations ():
    def __init__(self):
        pass

    # This method uses numpy to find the standard feviation of a variable.
    def calculate_deviation (self, data):
        return np.std(data, ddof = 1)

    
    #   This method is used to calculate teh coefficient of variation for the supplied data.
    def calculate_coefficient (self, data):
        return np.std(data, ddof = 1) / np.mean(data)
    
    #   This method is used to return the value found within the data range for the specified percentile.
    def calculate_percentile (self, data, column_name, percentile_range):
        target = pd.to_numeric(data[column_name], errors='coerce')
        target = target.dropna()

        if len(target) == 0:
            raise ValueError(f"No numeric data available in column '{column_name}' to calculate percentile.")
        
        return np.percentile(target, percentile_range)
    
    #   In essense this does the same as the method above, only it handles multiple percentile ranges at once.
    def calculate_multiple_percentiles(self, data, column_name, percentile_list):
        target = pd.to_numeric(data[column_name], errors='coerce')
        target = target.dropna()
        if len(target) == 0:
            raise ValueError(f"No numeric data available in column '{column_name}' to calculate percentiles.")
        
        return {p: np.percentile(target, p) for p in percentile_list}
    
    #   This method is used to calculate the variance of the supplied data.
    def calculate_variance (self, data):
        return np.var(data, ddof = 1)
    
    #   This method is used to generate a summary of all the columns at once.
    def summarize_all_columns(self, df):
        result = {}
        for col in df.select_dtypes(include=[np.number]).columns:
            col_data = df[col].dropna()
            result[col] = {
                "variance": self.calculate_variance(col_data),
                "std_dev": self.calculate_deviation(col_data),
                "coefficient": self.calculate_coefficient(col_data)
            }
        return pd.DataFrame(result).T