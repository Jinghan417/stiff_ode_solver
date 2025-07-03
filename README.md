# Stiff ODE Solver Comparison: The Robertson Problem

This project implements and compares four numerical solvers for stiff ordinary differential equations (ODEs) using the classic **Robertson problem** as a benchmark. The solvers included are:

- Forward Euler  
- Runge-Kutta 4 (RK4)  
- Backward Euler  
- Crank-Nicolson  

Users can input two different time step sizes. The script runs all four methods with both step sizes and generates side-by-side plots to compare solution behavior, accuracy, and stability under varying temporal resolution.

## Problem Definition

The Robertson problem is a well-known stiff ODE system defined by the following equations:


With initial conditions:  
y₁(0) = 1, y₂(0) = 0, y₃(0) = 0

## Features

- Modular solver implementations in Python (`methods/` directory)
- Input prompts for time interval and two custom step sizes
- Automatic visualization of all methods on two figures (one per step size)
- Designed for clear benchmarking and educational comparison

## Requirements

- Python 3.7+
- `matplotlib`
- `numpy`

Install dependencies with:

```bash
pip install matplotlib numpy
