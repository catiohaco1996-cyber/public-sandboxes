#!/usr/bin/env python3
"""Módulo que contiene la función islower."""


def islower(c):
    """Verifica si un carácter es una letra minúscula usando valores ASCII.

    Args:
        c (str): El carácter a evaluar.

    Returns:
        bool: True si es minúscula, False en caso contrario.
    """
    return ord('a') <= ord(c) <= ord('z')
