"""
    Funcion
"""
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
import numpy as np
import math


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
    return 1 * x+1


# Funcion cuadratica
def funcion_cuadratica(x):
    return 2*(x**2) + 5*x - 2

# Funcion seno


def funcion_seno(x):
    return math.sin(x)


# Ejercicio

def g(x):
    if x is not None:
        return x+1


def f(x):
    if x >= 0:
        return math.sqrt(x)


def fog(x):
    return f(g(x))


def gof(x):
    if x is not None:
        return g(f(x))


def main():
    # saludo("Aldo","Navarrete","Zamora")
    # paises("China","Rusia","Alemania")
    # ubicacion("CDMX")
    # print(suma(9, 5))
    # print(funcion_lineal(-1))

    # Funcion lineal

    # x = range(-100, 100)
    # plt.plot(x, [funcion_lineal(i) for i in x])
    # # poniendo el plano cartesiano
    # ax = plt.gca()
    # ax.spines["top"].set_color("none")
    # ax.spines["bottom"].set_position("zero")
    # ax.spines["left"].set_position("zero")
    # ax.spines["right"].set_color("none")
    # plt.xlim(-100, 100)
    # plt.ylim(-100, 100)
    # plt.title("Funcion Lineal", fontsize=20)
    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.grid()
    # plt.show()

    # Funcion cuadratica

    # x = range(-100, 100)
    # plt.plot(x, [funcion_cuadratica(i) for i in x])
    # # poniendo el plano cartesiano
    # ax = plt.gca()
    # ax.spines["top"].set_color("none")
    # ax.spines["bottom"].set_position("zero")
    # ax.spines["left"].set_position("zero")
    # ax.spines["right"].set_color("none")
    # plt.xlim(-20, 20)
    # plt.ylim(-15, 100)
    # plt.title("Funcion Cuadratica", fontsize=20)
    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.grid()
    # plt.show()

    # Funcion seno

    # x = range(-10, 10, 0.01)
    # plt.plot(x, [funcion_seno(i) for i in x])
    # # poniendo el plano cartesiano
    # ax = plt.gca()
    # ax.spines["top"].set_color("none")
    # ax.spines["bottom"].set_position("zero")
    # ax.spines["left"].set_position("zero")
    # ax.spines["right"].set_color("none")
    # plt.xlim(-20, 20)
    # plt.ylim(-1, 1)
    # plt.title("Funcion Seno", fontsize=20)
    # plt.xlabel('x')
    # plt.ylabel('f(x)')
    # plt.grid()
    # plt.show()

    # Ejercicio
    """"
    Sea f(x) = sqrt(x)
    y g(x) = x+1
    Entonctrar ambas graficas 
    Realizar f composicion g
    Realizar g composicion f
    """
    # Funcion f
    x = range(0, 50)
    plt.plot(x, [f(i) for i in x])
    # poniendo el plano cartesiano
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.title("Funcion f", fontsize=20)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()
    # Funcion g
    x = range(-50, 50)
    plt.plot(x, [g(i) for i in x])
    # poniendo el plano cartesiano
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.title("Funcion g", fontsize=20)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()

    # fog
    x = range(-50, 50)
    plt.plot(x, [fog(i) for i in x])
    # poniendo el plano cartesiano
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.title("Funcion g", fontsize=20)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()

    # gof
    x = range(-50, 50)
    plt.plot(x, [gof(i) for i in x])
    # poniendo el plano cartesiano
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    ax.spines["right"].set_color("none")
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.title("Funcion g o f (x)", fontsize=20)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()


main()
