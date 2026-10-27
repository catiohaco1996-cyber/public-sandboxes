#!/usr/bin/env python3
"""Módulo para la impresión segura de elementos de una lista."""


def safe_print_list(my_list=[], x=0):
    """Imprime x elementos de una lista de forma segura.

    Args:
        my_list (list): La lista que contiene los elementos.
        x (int): El número de elementos a imprimir.

    Returns:
        int: El número real de elementos que se lograron imprimir.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
