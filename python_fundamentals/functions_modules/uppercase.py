#!/usr/bin/env python3
"""Módulo que contiene la función uppercase."""


def uppercase(str):
    """Imprime una cadena de texto en mayúsculas usando conversión ASCII.

    Args:
        str (str): La cadena a convertir e imprimir.
    """
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
