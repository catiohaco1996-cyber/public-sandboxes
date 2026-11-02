#!/usr/bin/env python3
"""
Este módulo define la clase Rectangle que hereda de BaseGeometry.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Representa un rectángulo utilizando BaseGeometry para su validación.
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
