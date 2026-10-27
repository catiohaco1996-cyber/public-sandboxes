#!/usr/bin/env python3
"""Módulo para añadir cadenas de texto al final de un archivo."""


def append_write(filename="", text=""):
    """Añade una cadena al final de un archivo UTF-8 y devuelve los caracteres."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
