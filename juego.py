"""
Módulo que agrupa las funciones que describen la lógica interna del juego
"""

from entrada import (
    pedir_entrada_numero,
    pedir_entrada_numero_delimitado,
    pedir_entrada_si_o_no,
)
from entrada.menú import nivel_seleccionado
from entrada.numero import numero_adivinar


def jugar_una_vez(numero, minimo, maximo):
    intento = pedir_entrada_numero_delimitado("Adivine el numero", minimo, maximo)

    # Se comprueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        victoria = False
    else:
        print("¡Ha ganado!")
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo


def pedir_entrada_del_numero_incognita(minimo, maximo):
    return pedir_entrada_numero_delimitado("Introduzca el número a adivinar",
                                        minimo, maximo)


def jugar_una_partida(numero, minimo, maximo):
    while True:
        # Se entra en un bucle infinito
        # que permite jugar varias veces

        victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)

        if (victoria):
            return


def niveles():
    selector_nivel = nivel_seleccionado()
    if selector_nivel == 1:
        minimo = 0
        maximo = 100
    elif selector_nivel == 2:
        minimo = 0
        maximo = 1000
    elif selector_nivel == 3:
        minimo = 0
        maximo = 1000000
    else:
        minimo = 0
        maximo = 1000000000000
    return minimo, maximo


def jugar():
    minimo, maximo = niveles()
    while True:
        numero = numero_adivinar(minimo, maximo)
        jugar_una_partida(numero, minimo, maximo)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return

