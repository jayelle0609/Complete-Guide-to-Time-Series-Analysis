AR(1), AR(2), AR(3), and AR(4) models are **autoregressive (AR)** models of different orders used in time series analysis. They describe a process where the current value of a variable depends linearly on its previous values plus a random error term.

---

### 🔹 General Form of an AR(p) Model:

An **AR(p)** model is written as:

$$
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + \epsilon_t
$$

* $X_t$: current value of the time series at time $t$
* $c$: constant term (intercept)
* $\phi_1, \phi_2, \dots, \phi_p$: autoregressive coefficients
* $\epsilon_t$: white noise (random error) at time $t$

---

### 🔹 AR(1): First-order Autoregressive Model

$$
X_t = c + \phi_1 X_{t-1} + \epsilon_t
$$

* The current value depends only on the **immediately previous** value.
* Simple and often used when there's strong correlation between adjacent time points.

---

### 🔹 AR(2): Second-order Autoregressive Model

$$
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \epsilon_t
$$

* The current value depends on the last **two** values.
* Can model more complex dynamics like cycles.

---

### 🔹 AR(3): Third-order Autoregressive Model

$$
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + \epsilon_t
$$

* Uses the past **three** values.
* Allows for even more flexibility in modeling time dependencies.

---

### 🔹 AR(4): Fourth-order Autoregressive Model

$$
X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + \phi_4 X_{t-4} + \epsilon_t
$$

* Depends on the last **four** values.
* Useful when a process shows longer memory or lags.

---

### 🔸 Summary Table

| Model | Equation                                                                                   | Depends on... |
| ----- | ------------------------------------------------------------------------------------------ | ------------- |
| AR(1) | $X_t = c + \phi_1 X_{t-1} + \epsilon_t$                                                    | 1 lag         |
| AR(2) | $X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \epsilon_t$                                   | 2 lags        |
| AR(3) | $X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + \epsilon_t$                  | 3 lags        |
| AR(4) | $X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \phi_3 X_{t-3} + \phi_4 X_{t-4} + \epsilon_t$ | 4 lags        |

---

Let me know if you'd like to see examples, Python code, or when to choose which model.
