#!/usr/bin/env python3
"""Módulo que contiene la función print_last_digit."""


def print_last_digit(number):
    """Imprime y devuelve el último dígito positivo de un número.

    Args:
        number (int): El número a evaluar.

    Returns:
        int: El último dígito en valor positivo.
    """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
