#!/usr/bin/env python3
"""Módulo que contiene la función print_matrix_integer."""


def print_matrix_integer(matrix=[[]]):
    """Imprime una matriz de enteros formateada.

    Args:
        matrix (list): Lista de listas con números enteros.
    """
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))
