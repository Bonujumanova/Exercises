from math import sqrt

__all__ = ["triangle_perimeter", "triangle_area"]


def triangle_perimeter(
        a: int = 5, b: int = 7, c: int = 9
):
    P = a + b + c
    return P


def triangle_area(
        a: int = 5,
        b: int = 7,
        c: int = 9
):
    p = triangle_perimeter(a, b, c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s
