#!/usr/bin/env python3
"""Módulo que contiene la función replace_in_list."""


def replace_in_list(my_list, idx, element):
    """Reemplaza un elemento de una lista en una posición específica.

    Args:
        my_list (list): La lista original.
        idx (int): El índice donde se insertará el elemento.
        element: El nuevo elemento a colocar.

    Returns:
        list: La lista modificada o la original si idx está fuera de rango.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    my_list[idx] = element
    return my_list
