#!/usr/bin/env python3
"""
Este módulo define la clase Square que herede de Rectangle.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Representa un cuadrado que hereda de la clase Rectangle.
    """

    def __init__(self, size):
        """
        Inicializa una nueva instancia de Square.

        Args:
            size (int): El tamaño del lado del cuadrado.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
