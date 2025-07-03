def solve(func, y0, t0, t_end, h, tol=1e-10, max_iter=100):
    def newton(f, y_init, t_next):
        y = y_init
        for _ in range(max_iter):
            f_val = y - y_prev - h * f(t_next, y)
            dfdy = 1 + h * 15  # approximate df/dy for Robertson
            y_new = y - f_val / dfdy
            if abs(y_new - y) < tol:
                return y_new
            y = y_new
        return y

    ts = [t0]
    ys = [y0]
    t, y_prev = t0, y0
    while t < t_end:
        t_next = t + h
        y = newton(func, y_prev, t_next)
        ts.append(t_next)
        ys.append(y)
        t = t_next
        y_prev = y
    return ts, ys