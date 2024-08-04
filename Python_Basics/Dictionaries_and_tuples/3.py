import math


def circlecalci(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius

    return area, circumference, diameter


mathcalc = circlecalci(4)
print(mathcalc)



