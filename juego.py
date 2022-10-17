"""
Módulo que agrupa las funciones que describen la lógica interna del juego
"""

from entrada import (
    pedir_entrada_numero,
    pedir_entrada_numero_delimitado,
    pedir_entrada_si_o_no,
)
from entrada.menú import color_asignado, menu_completo, menu_inicio, texto_personalizado
from entrada.numero import numero_a_adivinar
import math

def puntuacion(maximo, vidas):
    puntuacion = math.log10(maximo)* 100 + vidas * 100
    return puntuacion


def jugar_una_vez(numero, minimo, maximo, vidas, puntos):
    intento = pedir_entrada_numero_delimitado("Adivine el numero", minimo, maximo)
    # Se comprueba si el intento es correcto o no
    if vidas == 1:
        color_asignado('red')(texto_personalizado("rectangles", "Game Over"))
        victoria = True
    elif intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        vidas-=1
        puntos -= 100
        print ("Tu puntuación es de {} puntos!".format(puntos))
        print("Le queda(n) {} intentos".format(vidas))
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        vidas-=1
        puntos -= 100
        print ("Tu puntuación es de {} puntos!".format(puntos))
        print("Le queda(n) {} intentos".format(vidas))
        victoria = False
    else:
        color_asignado('green')(texto_personalizado("rectangles", "Victoria"))
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo, vidas, puntos

def pedir_entrada_del_numero_incognita(minimo, maximo):
    return pedir_entrada_numero_delimitado("Introduzca el número a adivinar",
                                        minimo, maximo)


def jugar_una_partida(numero, minimo, maximo, vidas, puntos):
    while True:
        # Se entra en un bucle infinito
        # que permite jugar varias veces

        victoria, minimo, maximo, vidas, puntos = jugar_una_vez(numero, minimo, maximo, vidas, puntos)
        if (victoria):
            return puntos


def niveles():
    selector_nivel = menu_completo()
    if selector_nivel == 1:
        minimo = 0
        maximo = 100
        vidas = 10
    elif selector_nivel == 2:
        minimo = 0
        maximo = 1000
        vidas = 15
    elif selector_nivel == 3:
        minimo = 0
        maximo = 1000000
        vidas = 25
    else:
        minimo = 0
        maximo = 1000000000000
        vidas = 35
    puntos = puntuacion(maximo, vidas)
    return minimo, maximo, vidas, puntos

def jugar():
    minimo, maximo, vidas, puntos = niveles()
    while True:
        numero = numero_a_adivinar(minimo, maximo)
        jugar_una_partida(numero, minimo, maximo, vidas, puntos)

        if not pedir_entrada_si_o_no("Su puntuación ha sido de {} puntos!\n¿Desea jugar una nueva partida?".format(puntos)):
            print("¡Hasta pronto!")
            return

