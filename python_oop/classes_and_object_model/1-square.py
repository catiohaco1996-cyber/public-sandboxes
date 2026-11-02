#!/usr/bin/env python3
"""
Este módulo define la clase Square con un atributo privado.
"""


class Square:
    """
    Representa un cuadrado con un tamaño definido.
    """

    def __init__(self, size):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado.
        """
        self.__size = size
