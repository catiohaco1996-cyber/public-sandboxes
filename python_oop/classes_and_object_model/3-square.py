#!/usr/bin/env python3
"""
Este módulo define la clase Square con validaciones y un método de área.
"""


class Square:
    """
    Representa un cuadrado con validación de tamaño y cálculo de área.
    """

    def __init__(self, size=0):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado. Por defecto es 0.

        Raises:
            TypeError: Si size no es un número entero.
            ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcula el área del cuadrado.

        Returns:
            int: El área del cuadrado (size elevado al cuadrado).
        """
        return self.__size ** 2
