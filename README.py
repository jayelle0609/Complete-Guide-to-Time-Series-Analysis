# Complete-Guide-to-Time-Series-Analysis
# Autoregressive Models (AR)

Autoregressive (AR) models are used in time series analysis to describe a process where the current value depends on its previous values plus a random error.

---

## General AR(p) Model

\[
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + \epsilon_t
\]

- **\(X_t\)**: Value at time \(t\)
- **\(c\)**: Constant term
- **\(\phi_1, \dots, \phi_p\)**: AR coefficients
- **\(\epsilon_t\)**: White noise at time \(t\)

---

## AR(1): First-Order Model

\[
X_t = c + \phi_1 X_{t-1} + \epsilon_t
\]

- Depends on the **previous value**.

---

## AR(2): Second-Order Model

\[
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \epsilon_t
\]

- Depends on the **last two values**.

---

## AR(3): Third-Order Model

\[
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + \epsilon_t
\]

- Depends on the **last three values**.

---

## AR(4): Fourth-Order Model

\[
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + \phi_4 X_{t-4} + \epsilon_t
\]

- Depends on the **last four values**.

---

## Summary Table

| Model | Equation | Depends on... |
|-------|----------|----------------|
| AR(1) | \( X_t = c + \phi_1 X_{t-1} + \epsilon_t \) | 1 lag |
| AR(2) | \( X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \epsilon_t \) | 2 lags |
| AR(3) | \( X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + \epsilon_t \) | 3 lags |
| AR(4) | \( X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + \phi_4 X_{t-4} + \epsilon_t \) | 4 lags |

---

> **Note**: For code implementation in Python, you can use `statsmodels.tsa.ar_model.AutoReg`.
