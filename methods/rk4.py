def solve(func, y0, t0, t_end, h):
    ts = [t0]
    ys = [y0]
    t, y = t0, y0
    while t < t_end:
        k1 = func(t, y)
        k2 = func(t + h/2, y + h/2 * k1)
        k3 = func(t + h/2, y + h/2 * k2)
        k4 = func(t + h, y + h * k3)
        y += (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t += h
        ts.append(t)
        ys.append(y)
    return ts, ys