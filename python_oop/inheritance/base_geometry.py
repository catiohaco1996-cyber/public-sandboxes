#!/usr/bin/env python3
"""
Este módulo define la clase BaseGeometry.
"""


class BaseGeometry:
    """
    Clase base para operaciones y validaciones geométricas.
    """

    def area(self):
        """
        Lanza una excepción indicando que el método no está implementado.

        Raises:
            Exception: Siempre, con el mensaje 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valida que un parámetro de entrada sea un entero mayor que 0.

        Args:
            name (str): El nombre del parámetro (usado en mensajes de error).
            value (int): El valor a validar.

        Raises:
            TypeError: Si el valor no es un número entero.
            ValueError: Si el valor es menor o igual a 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
