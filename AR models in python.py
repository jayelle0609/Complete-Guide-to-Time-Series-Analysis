# Autoregressive Model (AR) Example for Beginners

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

# Step 1: Create a simple synthetic time series data
# Let's simulate an AR(1) process: X_t = 0.7 * X_{t-1} + noise

np.random.seed(42)  # for reproducibility
n = 100  # number of data points
phi = 0.7  # AR(1) coefficient
noise = np.random.normal(0, 1, size=n)

X = np.zeros(n)
for t in range(1, n):
    X[t] = phi * X[t-1] + noise[t]

# Step 2: Plot the generated time series
plt.plot(X)
plt.title("Simulated AR(1) Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()

# Step 3: Fit an AR model to the data using statsmodels
# We specify lags=1 since we know it's an AR(1) process
model = AutoReg(X, lags=1)
model_fit = model.fit()

# Step 4: Print the fitted coefficients
print("Fitted AR(1) coefficients:")
print(f"Intercept (c): {model_fit.params[0]:.3f}")
print(f"Phi_1: {model_fit.params[1]:.3f}")

# Step 5: Make predictions
pred_start = len(X)
pred_end = len(X) + 9  # predict 10 steps ahead
predictions = model_fit.predict(start=pred_start, end=pred_end, dynamic=False)

print("\nPredictions for next 10 time steps:")
print(predictions)

# Step 6 (Optional): Plot the original series with predictions
plt.plot(X, label='Observed')
plt.plot(range(pred_start, pred_end+1), predictions, 'r--', label='Forecast')
plt.legend()
plt.title("AR(1) Model Forecast")
plt.show()
