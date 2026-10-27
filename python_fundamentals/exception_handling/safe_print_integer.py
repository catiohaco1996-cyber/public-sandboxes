#!/usr/bin/env python3
"""Módulo para la impresión segura de un número entero."""


def safe_print_integer(value):
    """Imprime un entero con el formato {:d}.

    Args:
        value: El valor a imprimir (puede ser cualquier tipo).

    Returns:
        bool: True si es entero y se imprimió, False de lo contrario.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
