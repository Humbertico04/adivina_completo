from ast import Try
import pyfiglet
from termcolor import colored, cprint

"""
Variables para crear un menu interactivo y atractivo
"""
print_green = lambda x: cprint(x, 'green')
print_red = lambda x: cprint(x, 'red')
result = pyfiglet.figlet_format("Adivina el Numero", font = "epic"  )
print_green(result)
inicio=input("Presione enter para iniciar ")
print("\n")

# Nivel 1 (simple) (entre 0 y 100), 
# Nivel 2 (intermedio) (entre 0 y 1.000), 
# Nivel 3 (avanzado) (entre 0 y 1.000.000)
# Nivel 4 (experto) (entre 0 y 1.000.000.000.000)
 

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
    while True:
        selector_nivel=menu_seleccion()
        if 1<selector_nivel<5:
            break
        else: print_red("\n Solo están disponibles los niveles 1-4 \n")
    return selector_nivel
    
nivel_seleccionado()