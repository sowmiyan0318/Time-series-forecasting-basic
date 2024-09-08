import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample time series dataset
np.random.seed(0)
time_series = np.random.rand(100)

# Plot the time series data
plt.plot(time_series)
plt.show()

# Implement a simple moving average model
def moving_average(time_series, window_size):
    moving_averages = []
    for i in range(len(time_series) - window_size + 1):
        moving_averages.append(np.mean(time_series[i:i + window_size]))
    return moving_averages

# Forecast future values using the moving average model
window_size = 10
forecast = moving_average(time_series, window_size)

# Plot the forecasted values
plt.plot(time_series)
plt.plot(forecast)
plt.show()
