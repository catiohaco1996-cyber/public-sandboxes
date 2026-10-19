#!/usr/bin/env python3
"""Módulo que contiene la función update_dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Reemplaza o agrega un par clave/valor en un diccionario.

    Args:
        a_dictionary (dict): El diccionario a modificar.
        key (str): La clave a buscar o crear.
        value: El valor asociado a la clave.

    Returns:
        dict: El diccionario actualizado.
    """
    a_dictionary[key] = value
    return a_dictionary
