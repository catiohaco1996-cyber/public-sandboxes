#!/usr/bin/env python3
"""Módulo que contiene la función pow."""


def pow(a, b):
    """Calcula el valor de a elevado a la potencia de b usando un bucle.

    Args:
        a (int): La base.
        b (int): El exponente.

    Returns:
        int: El resultado de a^b.
    """
    if b == 0:
        return 1
    
    result = 1
    for _ in range(b):
        result *= a
    return result
