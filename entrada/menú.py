from ast import Try
import pyfiglet
from termcolor import colored, cprint

"""
Variables para crear un menu interactivo y atractivo
"""
print_green = lambda x: cprint(x, 'green')
print_red = lambda x: cprint(x, 'red')
 
def menu_visual(titulo):
    result = pyfiglet.figlet_format(titulo, font = "epic"  )
    print_green(result)
    inicio=input("Presione enter para iniciar ")
    print("\n")
    return result

"""
Esta función imprime el menu de selección del juego 
y recoge el nivel escogido por el usario.
"""
def menu_seleccion():
    while True:
        try:
            selector_nivel = int(input("Menu Inicio \n· Nivel 1 (simple) \n· Nivel 2 (intermedio) \n· Nivel 3 (avanzado) \n· Nivel 4 (experto) \nSeleccione un nivel: "))
            break
        except ValueError:
            print("Solo están disponibles los niveles 1-4")
    return selector_nivel

"""
Esta función utiliza la anterior y agrega una post-condición
sobre los extremos del número a introducir.
"""
def nivel_seleccionado():
    menu_visual("Adivina el Numero")
    while True:
        selector_nivel=menu_seleccion()
        if 0<selector_nivel<5:
            break
        else: print_red("\n Solo están disponibles los niveles 1-4 \n")
    return selector_nivel