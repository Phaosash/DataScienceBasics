import numpy as np

Pulse_Rates = [80, 85, 90, 95, 100, 105, 110, 110, 120, 125]
Calorie_burn_rates = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

#   Gets the highest value from the pulse rate array
Average_pulse_max = max(Pulse_Rates)

#   Gets the lowest value from the pulse rate array
Average_Pulse_Min = min(Pulse_Rates)

#   Calculates the average calorie burn rate
Average_burn_rate = np.mean(Calorie_burn_rates)

print (f"Max recorded pulse rate: {Average_pulse_max}")
print (f"Lowest recorded pulse rate: {Average_Pulse_Min}")
print (f"Average amount of calories burned: {Average_burn_rate}")