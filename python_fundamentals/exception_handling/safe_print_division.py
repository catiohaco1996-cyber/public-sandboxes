#!/usr/bin/env python3
"""Módulo para realizar una división segura entre dos enteros."""


def safe_print_division(a, b):
    """Divide dos enteros e imprime el resultado usando finally.

    Args:
        a (int): El numerador.
        b (int): El denominador.

    Returns:
        float o None: El resultado de la división o None si falló.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
