#!/usr/bin/env python3
"""Módulo que contiene la función print_list_integer."""


def print_list_integer(my_list=[]):
    """Imprime todos los enteros de una lista, uno por línea.

    Args:
        my_list (list): Lista de enteros a imprimir.
    """
    for item in my_list:
        print("{:d}".format(item))
