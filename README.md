#  Stiff ODE Solver Comparison using the Robertson Problem

This project implements and compares four numerical methods—Euler, Runge-Kutta 4 (RK4), Backward Euler, and Crank-Nicolson—on the classic stiff system known as the **Robertson problem**. It allows users to input two different time step sizes and visualizes the effect of step size on numerical accuracy and stability.

---

##  Project Features

- Implements 4 common ODE solvers
- Supports stiff systems (nonlinear implicit solvers included)
- Accepts two user-defined step sizes at runtime
- Creates side-by-side plots of solver results for comparison
- Uses Python and `matplotlib` for visualization

---

##  The Robertson Problem

This system of stiff ODEs is defined as:

\[
\begin{cases}
\frac{dy_1}{dt} = -0.04 y_1 + 10^4 y_2 y_3 \\
\frac{dy_2}{dt} = 0.04 y_1 - 10^4 y_2 y_3 - 3 \times 10^7 y_2^2 \\
\frac{dy_3}{dt} = 3 \times 10^7 y_2^2
\end{cases}
\]

Initial conditions:
```python
y0 = [1.0, 0.0, 0.0]
t0 = 0
t_end = 1e3
