from ast import Try
from turtle import color
import pyfiglet
from termcolor import colored, cprint


def color_asignado(color):
    """
    Esta función añade color. El color debe estar entre ''
    """
    print_color = lambda x: cprint(x, color)
    return print_color


def texto_personalizado(fuente, titulo):
    """
    Esta crea un texto personalizado. La fuente y el titulo deben estar entre ""
    """
    result = pyfiglet.figlet_format(titulo, font = fuente  )
    return result


def menu_inicio():
    """
    Esta función crea el menu personalizado
    """
    result = texto_personalizado("epic", "Adivina el Numero")
    color_asignado('green')(result)
    input("Presione enter para iniciar ")
    print("\n")
    return 


def menu_seleccion():
    """
    Esta función imprime el menu de selección del juego 
    y recoge el nivel escogido por el usario.
    """
    while True:
        try:
            selector_nivel = int(input("Menu Inicio \n· Nivel 1 (simple) \n· Nivel 2 (intermedio) \n· Nivel 3 (avanzado) \n· Nivel 4 (experto) \nSeleccione un nivel: "))
            break
        except ValueError:
            print("Solo están disponibles los niveles 1-4")
    return selector_nivel


def menu_completo():
    """
    Esta función utiliza la anterior y agrega una post-condición
    sobre los extremos del número a introducir, además de juntar todo el menú.
    """
    menu_inicio()
    while True:
        selector_nivel=menu_seleccion()
        if 0<selector_nivel<5:
            break
        else: color_asignado('red')("\n Solo están disponibles los niveles 1-4 \n")
    return selector_nivel