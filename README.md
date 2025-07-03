# Stiff ODE Solver Comparison

This project implements and compares four numerical solvers for stiff ordinary differential equations (ODEs) using a simplified linear test equation as a benchmark. The solvers included are:

- Forward Euler  
- Runge–Kutta 4 (RK4)  
- Backward Euler  
- Crank–Nicolson  

Users can input two different time step sizes. The script runs all four methods with both step sizes and generates side-by-side plots to compare solution behavior, accuracy, and stability.

## Test Equation

The ODE used for comparison is a simple linear stiff equation:

``dy/dt = -15y + 15*cos(t)``

with initial condition \( y(0) = 0 \). This equation exhibits stiffness due to the large negative coefficient, making it suitable for evaluating solver performance on stiff problems.

## Features

- Modular solver implementations in Python (`methods/` directory)  
- Interactive input for time interval and two custom step sizes  
- Automatic visualization of results for both time steps  
- Designed for educational use and benchmarking solver stability  

## Requirements

- Python 3.7+  
- `matplotlib`  
- `numpy`  

Install dependencies with:

```bash
pip install matplotlib numpy
