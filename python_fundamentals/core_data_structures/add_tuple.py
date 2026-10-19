#!/usr/bin/env python3
"""Módulo que contiene la función add_tuple."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Suma los dos primeros elementos de dos tuplas.

    Trata los valores faltantes como 0.

    Args:
        tuple_a (tuple): Primera tupla.
        tuple_b (tuple): Segunda tupla.

    Returns:
        tuple: Una nueva tupla con exactamente dos enteros.
    """
    # Extraer el primer elemento o usar 0 si no existe
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    # Extraer el segundo elemento o usar 0 si no existe
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)
