import numpy as np
import matplotlib.pyplot as plt

def plot(titulo, xmax, ymax):
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xlim(0, xmax); plt.ylim(0, ymax)
    plt.xlabel('Caminhão Pequeno (x)')
    plt.ylabel('Caminhão Grande (y)')
    plt.legend()
    plt.title(titulo)

# Restrição 1: 4x + 7y = 28
def y1(x):
    return (28 - 4*x) / 7

# Restrição 2: x + y = 8
def y2(x):
    return 8 - x

# Função objetivo: Custo
def objective(x, y):
    return 200*x + 300*y

def plot_restricoes(x):
    plt.plot(x, y1(x), label='4x + 7y = 28')
    plt.plot(x, y2(x), label='x + y = 8')

def area_factibilidade(x):
    y_r1 = y1(x)
    y_r2 = y2(x)

    # Região viável = acima de y1 (≥) e abaixo de y2 (≤)
    y_feasible = np.minimum(y_r2, ymax)
    y_feasible = np.maximum(y_feasible, y_r1)

    plt.fill_between(
        x, y_r1, y_r2,
        where=(y_r2 >= y_r1) & (y_r1 >= 0),
        color='gray', alpha=0.5, label='Região Viável'
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
    global ymax
    xmax = 10
    ymax = 10
    x = np.linspace(0, xmax, 400)

    plt.figure(figsize=(6,6))
    plot('Problema de Transporte', xmax, ymax)
    plot_restricoes(x)
    area_factibilidade(x)
    curvas_nivel(xmax, ymax)

    plt.show()

if __name__ == '__main__':
    main()
