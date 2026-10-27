#!/usr/bin/env python3
"""Módulo para lanzar una excepción NameError con un mensaje."""


def raise_exception_msg(message=""):
    """Provoca una excepción NameError incluyendo un mensaje personalizado.

    Args:
        message (str): El mensaje de texto que se adjuntará al error.

    Raises:
        NameError: Se lanza siempre con el mensaje indicado.
    """
    raise NameError(message)
