#!/usr/bin/env python3
"""
Este módulo define la clase Rectangle que hereda de BaseGeometry.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Representa un rectángulo utilizando BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Inicializa una nueva instancia de Rectangle.

        Args:
            width (int): El ancho del rectángulo.
            height (int): El alto del rectángulo.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calcula el área del rectángulo.

        Returns:
            int: El área del rectángulo.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Define la representación en cadena de la instancia Rectangle.

        Returns:
            str: Una descripción formateada del rectángulo.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
