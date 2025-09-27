from pulp import LpMaximize, LpProblem, LpVariable, lpSum
import numpy as np
import matplotlib.pyplot as plt

def plot(titulo, xmax, ymax):
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xlim(0, xmax); plt.ylim(0, ymax)
    plt.xlabel('Produto A (x)')
    plt.ylabel('Produto B (y)')
    plt.legend()
    plt.title(titulo)

# Restrição 1: x + 2y = 80  -> y = (80 - x)/2
def y1(x):
    return (80 - x)/2

# Restrição 2: 2x + y = 100 -> y = 100 - 2x
def y2(x):
    return 100 - 2*x

# Função objetivo: Lucro = 40x + 60y
def objective(x, y):
    return 40*x + 60*y

def plot_restricoes(x):
    plt.plot(x, y1(x), label='x + 2y ≤ 80 (Máquina)')
    plt.plot(x, y2(x), label='2x + y ≤ 100 (Montagem)')

def gradiente():
    # vetor gradiente = (40,60)
    plt.arrow(0, 0, 10, 15, head_width=1, head_length=1.5,
              fc='red', ec='red', label='Gradiente (40,60)')

def area_factibilidade(x):
    y_feasible = np.minimum(y1(x), y2(x))
    plt.fill_between(
        x, 0, y_feasible,
        where=(y_feasible > 0),
        color='gray', alpha=0.5,
        label='Região Viável'
    )

def curvas_nivel(xmax, ymax):
    x_grid = np.arange(0, xmax+1, 1)
    y_grid = np.arange(0, ymax+1, 1)

    X, Y = np.meshgrid(x_grid, y_grid)
    Z = objective(X, Y)

    contour = plt.contour(X, Y, Z, levels=20, colors='k',
                          linestyles='--', linewidths=1.2)
    plt.clabel(contour, inline=True, fontsize=8)

def main():
    xmax = 60
    ymax = 60
    x = np.linspace(0, xmax, 400)
    plt.figure(figsize=(6,6))

    plot('Programação Linear - Lucro da Fábrica', xmax, ymax)
    plot_restricoes(x)
    gradiente()
    area_factibilidade(x)
    curvas_nivel(xmax, ymax)

    plt.show()

if __name__ == '__main__':
    main()
