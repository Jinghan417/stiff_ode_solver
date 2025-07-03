import matplotlib.pyplot as plt

def plot_all(solutions, h):
    plt.figure(figsize=(10, 6))  # 每次绘图前开启新图

    for method, (t_vals, y_vals) in solutions.items():
        plt.plot(t_vals, y_vals, label=method)

    plt.xlabel("t")
    plt.ylabel("y")
    plt.title(f"Robertson Stiff ODE Comparison (Step Size h = {h})")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

