
````markdown
# Introduction to Autoregressive (AR) Models with Python Example

Autoregressive (AR) models are used in time series analysis to predict a value based on its own previous values. They are simple yet powerful tools for understanding how data evolves over time.

---

## What is an AR Model?

An **AR(p)** model expresses the current value \(X_t\) as a linear combination of the previous \(p\) values plus some random noise:

\[
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + \epsilon_t
\]

- \(X_t\): value at time \(t\)  
- \(c\): constant (intercept)  
- \(\phi_1, \phi_2, \dots, \phi_p\): coefficients that capture the influence of past values  
- \(\epsilon_t\): noise term  

---

## Python Example: Simulating and Fitting an AR(1) Model

This example demonstrates how to simulate a simple AR(1) time series, fit an AR(1) model using Python's `statsmodels`, and forecast future values.

---

### Step 1: Import Libraries and Simulate AR(1) Time Series

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n = 100        # Number of data points
phi = 0.7      # AR(1) coefficient

# Generate white noise
noise = np.random.normal(0, 1, size=n)

# Initialize time series array
X = np.zeros(n)

# Simulate AR(1): X_t = phi * X_{t-1} + noise_t
for t in range(1, n):
    X[t] = phi * X[t-1] + noise[t]
````

---

### Step 2: Plot the Simulated Time Series

```python
plt.plot(X)
plt.title("Simulated AR(1) Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
```

---

### Step 3: Fit an AR(1) Model Using statsmodels

```python
# Fit AR(1) model
model = AutoReg(X, lags=1)
model_fit = model.fit()

# Display estimated parameters
print("Fitted AR(1) coefficients:")
print(f"Intercept (c): {model_fit.params[0]:.3f}")
print(f"Phi_1: {model_fit.params[1]:.3f}")
```

---

### Step 4: Forecast Future Values

```python
# Predict next 10 steps
pred_start = len(X)
pred_end = len(X) + 9
predictions = model_fit.predict(start=pred_start, end=pred_end, dynamic=False)

print("\nPredictions for next 10 time steps:")
print(predictions)
```

---

### Step 5: Plot Original Data with Forecasts

```python
plt.plot(X, label='Observed')
plt.plot(range(pred_start, pred_end + 1), predictions, 'r--', label='Forecast')
plt.legend()
plt.title("AR(1) Model Forecast")
plt.show()
```

---

## Summary

* AR models help predict future points by regressing on past values.
* The order $p$ indicates how many previous points influence the current value.
* Python’s `statsmodels` library makes fitting AR models straightforward.
* Start with simple models (e.g., AR(1)) and increase complexity as needed.

---

Feel free to experiment with different AR orders by changing the `lags` parameter in `AutoReg`.

---

If you want, I can help you create similar examples for AR(2), AR(3), or ARIMA models next!

```

---

Just copy everything from the triple backticks above, paste it into your `.md` file, and GitHub will nicely render your text, math, and code blocks.

Let me know if you want me to add anything else!
```
