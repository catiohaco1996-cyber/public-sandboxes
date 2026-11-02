#!/usr/bin/env python3
"""
Este módulo define la clase Square con getters, setters y método de área.
"""


class Square:
    """
    Representa un cuadrado con validación de tamaño, propiedades y área.
    """

    def __init__(self, size=0):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado. Por defecto es 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Obtiene el tamaño actual del cuadrado.

        Returns:
            int: El tamaño del lado del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Establece el tamaño del cuadrado aplicando validaciones.

        Args:
            value (int): El nuevo tamaño para el lado del cuadrado.

        Raises:
            TypeError: Si value no es un número entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcula el área del cuadrado.

        Returns:
            int: El área del cuadrado.
        """
        return self.__size ** 2

