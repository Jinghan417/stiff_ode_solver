from methods import euler, rk4, backward_euler, crank_nicolson

def solve_all_methods(func, y0, t0, t_end, h):
    return {
        "Euler": euler.solve(func, y0, t0, t_end, h),
        "RK4": rk4.solve(func, y0, t0, t_end, h),
        "Backward Euler": backward_euler.solve(func, y0, t0, t_end, h),
        "Crank-Nicolson": crank_nicolson.solve(func, y0, t0, t_end, h)
    }
