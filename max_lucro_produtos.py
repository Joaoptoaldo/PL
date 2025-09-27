from pulp import LpMaximize, LpProblem, LpVariable, lpSum
import numpy as np
import matplotlib.pyplot as plt

def plot(titulo, xmax, ymax):
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xlim(0,xmax); plt.ylim(0,ymax)
    plt.xlabel('Produto 1 (x)')
    plt.ylabel('Produto 2 (y)')
    plt.legend()
    plt.title(titulo)

# Restrições:
# 1) x + y <= 10
# 2) 1*x + 2*y <= 16  (Recurso B)
# 3) 2*x + 1*y <= 19  (Recurso C)

def y1(x):
    return 10 - x             # x + y <= 10

def y2(x):
    return (16 - 1*x)/2       # 1*x + 2*y <= 16

def y3(x):
    return 19 - 2*x           # 2*x + 1*y <= 19

# Função objetivo Z = x + y
def objective(x,y):
    return x + y

def plot_resticoes(x):
    plt.plot(x, y1(x), label='x + y = 10')
    plt.plot(x, y2(x), label='x + 2y = 16')
    plt.plot(x, y3(x), label='2x + y = 19')

def gradiente():
    # Gradiente da função objetivo Z = x + y
    plt.arrow(0,0,6,6, head_width=1, head_length=1.5, fc='red', ec='red', label='Gradiente')

def area_factibilidade(x):
    y_feasible = np.minimum(np.minimum(y1(x), y2(x)), y3(x))
    plt.fill_between(
        x, 0, y_feasible,
        where=(y_feasible > 0),
        color='gray', alpha=0.5,
        label='Região Viável'
    )

def curvas_nivel(xmax, ymax):
    x_grid = np.arange(0,xmax+1,1)
    y_grid = np.arange(0,ymax+1,1)
    X, Y = np.meshgrid(x_grid, y_grid)
    Z = objective(X,Y)
    contour = plt.contour(X, Y, Z, levels=20, colors='k', linestyles='--', linewidths=1)
    plt.clabel(contour, inline=True, fontsize=8)

def main():
    xmax = 12  # limite maior que possível para visualização
    ymax = 12
    x = np.linspace(0, xmax, 400)
    plt.figure(figsize=(6,6))
    
    plot('Programação Linear - Exemplo', xmax, ymax)
    plot_resticoes(x)
    gradiente()
    area_factibilidade(x)
    curvas_nivel(xmax, ymax)
    
    plt.show()

if __name__ == '__main__':
    main()
