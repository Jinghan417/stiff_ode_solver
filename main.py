from equation import stiff_example
from solver import solve_all_methods
from visualizer import plot_all

if __name__ == '__main__':
    y0 = 0
    t0 = 0
    t_end = 5
    try:
        h1 = float(input("Enter the first step size (e.g., 0.01): "))
    except ValueError:
        print("Invalid input. Using default h1 = 0.01")
        h1 = 0.01

    try:
        h2 = float(input("Enter the second step size (e.g., 0.001): "))
    except ValueError:
        print("Invalid input. Using default h2 = 0.001")
        h2 = 0.001

    for h in [h1, h2]:
        solutions = solve_all_methods(stiff_example, y0, t0, t_end, h)
        plot_all(solutions, h)