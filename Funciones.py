"""
    Funcion
"""
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
import numpy as np


def saludo(nombre, apellido_paterno, apellido_materno):
    print(f"Hola {nombre} {apellido_paterno} {apellido_materno}!")


# Cuando mandas argumentos con asterisco se mandan como tuplas
def paises(*pais):
    print("Los paises que mandaste son: ", pais)


# Ubicacion
def ubicacion(ubi="CDMX"):
    print("Me ubico en {}".format(ubi))


# Suma
def suma(a, b):
    return a + b


# Funcion lineal
def funcion_lineal(x):
    return 1 * x


def on_move(event):
    # get the x and y pixel coords
    x, y = event.x, event.y
    if event.inaxes:
        ax = event.inaxes  # the axes instance
        print("data coords %f %f" % (event.xdata, event.ydata))


def on_click(event):
    if event.button is MouseButton.LEFT:
        print("disconnecting callback")
        plt.disconnect(binding_id)


def main():
    # saludo("Aldo","Navarrete","Zamora")
    # paises("China","Rusia","Alemania")
    # ubicacion("CDMX")
    # print(suma(9, 5))
    # print(funcion_lineal(-1))

    x = range(-100, 100)
    plt.plot(x, [funcion_lineal(i) for i in x])
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.grid()
    plt.show()


main()
