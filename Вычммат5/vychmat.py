import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(x+1) - (1/x)

def plot_graph():
    x_vals = np.linspace(0.5, 2, 100)
    y_vals = f(x_vals)
    
    plt.plot(x_vals, y_vals)
    plt.axhline(0, color='pink', linewidth=3)
    plt.grid(True)
    plt.show()

plot_graph()

def df(x):
    return (1 / (2 * np.sqrt(x + 1))) + (1 / x**2)
