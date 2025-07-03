def solve(func, y0, t0, t_end, h, tol=1e-10, max_iter=100):
    def fixed_point(y_prev, t, t_next):
        y = y_prev
        for _ in range(max_iter):
            f_avg = 0.5 * (func(t, y_prev) + func(t_next, y))
            y_new = y_prev + h * f_avg
            if abs(y_new - y) < tol:
                return y_new
            y = y_new
        return y

    ts = [t0]
    ys = [y0]
    t, y_prev = t0, y0
    while t < t_end:
        t_next = t + h
        y = fixed_point(y_prev, t, t_next)
        ts.append(t_next)
        ys.append(y)
        t = t_next
        y_prev = y
    return ts, ys