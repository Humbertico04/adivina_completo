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

def jugar_una_vez(numero, minimo, maximo, vidas):
    intento = pedir_entrada_numero_delimitado("Adivine el numero", minimo, maximo)
    # Se comprueba si el intento es correcto o no
    if vidas == 1:
        color_asignado('red')(texto_personalizado("rectangles", "Game Over"))
        victoria = True
    elif intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        vidas-=1
        print("Le queda(n) {} intentos".format(vidas))
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        vidas-=1
        print("Le queda(n) {} intentos".format(vidas))
        victoria = False
    else:
        color_asignado('green')(texto_personalizado("rectangles", "Victoria"))
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo, vidas


def pedir_entrada_del_numero_incognita(minimo, maximo):
    return pedir_entrada_numero_delimitado("Introduzca el número a adivinar",
                                        minimo, maximo)


def jugar_una_partida(numero, minimo, maximo, vidas):
    while True:
        # Se entra en un bucle infinito
        # que permite jugar varias veces

        victoria, minimo, maximo, vidas = jugar_una_vez(numero, minimo, maximo, vidas)
        if (victoria):
            return


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
    return minimo, maximo, vidas


def jugar():
    minimo, maximo, vidas = niveles()
    while True:
        numero = numero_a_adivinar(minimo, maximo)
        jugar_una_partida(numero, minimo, maximo, vidas)
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return

