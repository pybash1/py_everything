import math

pi: float = math.pi
e: float = math.e


def areaRect(length: float, breadth: float) -> float:
    """Finds area of rectangle"""
    area: float = length * breadth

    return area


def perimeterRect(length: float, breadth: float) -> float:
    """Finds perimeter of rectangle"""
    perimeter: float = 2 * (length + breadth)

    return perimeter


def areaSqr(side: float) -> float:
    """Finds area of square"""
    area: float = side ** 2

    return area


def perimeterSqr(side: float) -> float:
    """Finds perimeter of square"""
    perimeter: float = 4 * side

    return perimeter


def areaTriangle(base: float, height: float) -> float:
    """Finds area of triangle"""
    area: float = (height * base) / 2

    return area


def perimeterTriangle(side1: float, side2: float, base: float) -> float:
    """Finds perimeter of triangle"""
    perimeter: float = side1 + base + side2
    return perimeter


def areaCirc(radius: float) -> float:
    """Finds area of circle"""
    area: float = pi * radius * radius

    return area


def circumferenceCirc(radius: float) -> float:
    """Finds circumference of circle"""
    area: float = 2 * pi * radius

    return area


def volCyl(radius: float, height: float) -> float:
    """Finds volume of a cylinder"""
    volume: float = pi * radius * radius * height

    return volume


def volCone(radius: float, height: float) -> float:
    """Finds volume of a cone"""
    volume: float = pi * radius * radius * height / 3

    return volume


def volSphere(radius: float) -> float:
    """Finds volume of a sphere"""
    volume: float = 4 / 3 * pi * radius * radius * radius

    return volume


def volCube(edge: float) -> float:
    """Finds volume of a cube"""
    volume: float = edge ** 3

    return volume


def volCuboid(length: float, breadth: float, height: float) -> float:
    """Finds volume of a cuboid"""
    volume: float = length * breadth * height

    return volume


def pival() -> float:
    """Returns value of pi"""
    return pi


def eval_() -> float:
    """Returns value of e"""
    return e
