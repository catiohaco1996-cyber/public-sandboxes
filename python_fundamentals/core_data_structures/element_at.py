#!/usr/bin/env python3
"""Módulo que contiene la función element_at."""


def element_at(my_list, idx):
    """Recupera un elemento de una lista de manera segura (estilo C).

    Args:
        my_list (list): La lista de elementos.
        idx (int): El índice del elemento a recuperar.

    Returns:
        El elemento en la posición idx, o None si está fuera de rango.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
