#!/usr/bin/env python3
"""Módulo para imprimir únicamente enteros de una lista."""


def safe_print_list_integers(my_list=[], x=0):
    """Imprime los primeros x elementos de una lista que sean enteros.

    Args:
        my_list (list): La lista que contiene los elementos.
        x (int): El número de elementos a iterar.

    Returns:
        int: La cantidad real de enteros impresos.
    """
    count = 0
    for i in range(x):
        value = my_list[i]
        try:
            print("{:d}".format(value), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
