#!/usr/bin/env python3
"""Módulo para la lectura de archivos de texto."""


def read_file(filename=""):
    """Lee un archivo de texto en UTF-8 e imprime su contenido en stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

