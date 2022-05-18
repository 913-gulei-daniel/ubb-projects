"""
    Custom Exceptions for Graphs
"""


class VertexException(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class EdgeException(Exception):
    def __init__(self, message=""):
        super().__init__(message)
