import numpy as np
import matplotlib.pyplot as plt

def plot(titulo, xmax, ymax):
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xlim(0,xmax);plt.ylim(0,ymax)
    plt.xlabel('eixo - x')
    plt.ylabel('eixo - y')
    plt.legend()
    plt.title(titulo)

#2x + 4y = 100
def y1(x):
    return 25 - 0.5*x
#4x + 3y = 120
def y2(x):
    return 40 - (4/3)*x
#Z = 30x + 50y
def objective(x,y):
    return 30*x + 50*y
def plot_resticoes(x):
    plt.plot (x, y1(x), label = '2x + 4y = 100')
    plt.plot (x, y2(x), label = '4x + 3y = 120')

def gradiente():
    plt.arrow(0,0,6,10, head_width=1, head_length=1.5, 
              fc='red', ec = 'red', label ='Gradiente')

def area_factibilidade(x):
    y_feasible = np.minimum(y1(x), y2(x))

    plt.fill_between(
        x, 0, y_feasible,
        where=(y_feasible > 0),
        color = 'gray', alpha = 0.5,
        label = 'Região Viável'
    )

def curvas_nivel(xmax, ymax):
    x_grid = np.arange(0,xmax+1, 1)
    y_grid = np.arange(0,ymax+1, 1)

    X,Y = np.meshgrid(x_grid, y_grid)

    Z = objective(X,Y)

    contour = plt.contour(X, Y, Z, levels = 20, colors = 'k',
                          linestyles = '--', linewidths=1.2)
    plt.clabel(contour, inline= True, fontsize = 8)


def main():
    xmax = 60
    ymax = 60
    x = np.linspace(0,xmax, 400)
    plt.figure(figsize=(5,5))

    plot('PL', xmax, ymax)
    plot_resticoes(x)
    gradiente()
    area_factibilidade(x)
    curvas_nivel(xmax, ymax)

    plt.show()

if __name__ == '__main__':
    main()
