#!/usr/bin/env python3
"""Módulo para importar una función de suma e imprimir un formato."""
from add_0 import add

if __name__ == "__main__":
    if 'a' not in locals():
        a = 1
    if 'b' not in locals():
        b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
