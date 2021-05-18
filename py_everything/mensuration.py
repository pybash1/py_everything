import math

pi = math.pi
e = math.e

def areaRect(length: float, breadth: float) -> float:
    area = length * breadth
    
    return area

def perimeterRect(length: float, breadth: float) -> float:
    perimeter = 2 * (length + breadth)
    
    return perimeter

def areaSqr(side: float) -> float:
    area = side * side
    
    return area

def perimeterSqr(side: float) -> float:
    perimeter = 4 * side
    
    return perimeter

def areaTriangle(base: float, height: float) -> float:
    area = (height * base) / 2
    
    return area

def perimeterTriangle(side1: float, side2: float, base: float) -> float:
    perimeter = side1 + base + side2
    return perimeter

def areaCirc(radius: float) -> float:
    area = pi * radius * radius
    
    return area

def circumferenceCirc(radius: float) -> float:
    area = 2 * pi * radius
    
    return area

def volCyl(radius:float, height: float) -> float:
    volume = pi * radius * radius * height
    
    return volume

def volCone(radius:float, height: float) -> float:
    volume = pi * radius * radius * height / 3
    
    return volume

def volSphere(radius: float) -> float:
    volume = 4/3 * pi * radius * radius * radius
    
    return volume

def volCube(edge: float) -> float:
    volume = edge * edge * edge
    
    return volume

def volCuboid(length: float, breadth: float, height: float) -> float:
    volume = length * breadth * height
    
    return volume

def pival() -> float:
    return pi

def eval_() -> float:
    return e
