from DataManager import DataManager
from StatisticsCalculations import Calculations
from CorrelationCoefficients import CorrCalcs

dm = DataManager()
data = dm.get_loaded_data()

sc = Calculations()

cc = CorrCalcs()

#   The describe function is used to sumamrise the data
print(data.describe())

#   This prints out the 10% percentile for the Max_Pulse value
tenth_percentile = sc.calculate_percentile(data, "Max_Pulse", 10)
print(f"10th percentile of Max_Pulse: {tenth_percentile}")

# This is an example of how to get multiple percentiles at once
percentiles = sc.calculate_multiple_percentiles(data, "Max_Pulse", [10, 25, 50, 75, 90])
print("Percentiles of Max_Pulse:", percentiles)

#   This outputs the result of the standard deviation calculation
print(f"The calculated standard deciation is: {sc.calculate_deviation(data)}")

# This outputs the resilt of the coefficient of variation calculation
print(f"The calculated coefficient is: {sc.calculate_coefficient(data)}")

print(sc.calculate_variance(data))

summary_stats = sc.summarize_all_columns(data)
print(summary_stats)

cc.display_positive_plot(data, 'Average_Pulse', 'Calorie_Burnage')