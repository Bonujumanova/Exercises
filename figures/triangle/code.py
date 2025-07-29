from math import sqrt

def triangle_perimeter(a, b, c):
    P = a + b + c
    return P


def triangle_area(a, b, c):
    p = triangle_perimeter(a, b, c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s

a: int = 5
b: int = 7
c: int = 9
triangle_perimeter(a, b, c)
print(triangle_area(a, b, c))
