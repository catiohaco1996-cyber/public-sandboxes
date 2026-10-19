#!/usr/bin/env python3
"""Módulo que contiene la función best_score."""


def best_score(a_dictionary):
    """Devuelve la clave con el valor entero más grande del diccionario.

    Args:
        a_dictionary (dict): Diccionario con claves y puntuaciones.

    Returns:
        str: La clave con la mayor puntuación, o None si no es válido.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
