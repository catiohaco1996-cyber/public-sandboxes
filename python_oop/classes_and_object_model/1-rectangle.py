#!/usr/bin/env python3
"""
Este módulo define la clase Rectangle con propiedades de ancho y alto.
"""


class Rectangle:
    """
    Representa un rectángulo con validaciones para sus dimensiones.
    """

    def __init__(self, width=0, height=0):
        """
        Inicializa una nueva instancia de Rectangle.

        Args:
            width (int): El ancho del rectángulo. Por defecto es 0.
            height (int): El alto del rectángulo. Por defecto es 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Obtiene el ancho actual del rectángulo.

        Returns:
            int: El ancho del rectángulo.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Establece el ancho del rectángulo aplicando validaciones.

        Args:
            value (int): El nuevo ancho para el rectángulo.

        Raises:
            TypeError: Si value no es un número entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Obtiene el alto actual del rectángulo.

        Returns:
            int: El alto del rectángulo.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Establece el alto del rectángulo aplicando validaciones.

        Args:
            value (int): El nuevo alto para el rectángulo.

        Raises:
            TypeError: Si value no es un número entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

