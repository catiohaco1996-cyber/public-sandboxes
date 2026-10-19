#!/usr/bin/env python3
"""Módulo que contiene la función common_elements."""


def common_elements(set_1, set_2):
    """Devuelve un conjunto de elementos comunes en dos conjuntos.

    Args:
        set_1 (set): Primer conjunto.
        set_2 (set): Segundo conjunto.

    Returns:
        set: Un nuevo conjunto con los elementos comunes.
    """
    return set_1 & set_2
