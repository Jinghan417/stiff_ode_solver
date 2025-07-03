def solve(func, y0, t0, t_end, h):
    ts = [t0]
    ys = [y0]
    t, y = t0, y0
    while t < t_end:
        y += h * func(t, y)
        t += h
        ts.append(t)
        ys.append(y)
    return ts, ys
