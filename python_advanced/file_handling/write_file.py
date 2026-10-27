#!/usr/bin/env python3
"""Módulo para la escritura de cadenas de texto en archivos."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo en UTF-8 y devuelve los caracteres."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
