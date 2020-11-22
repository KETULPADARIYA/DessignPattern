from enum import Enum


class Color(Enum):
    RED =1
    GREEN =2
    BLUE =3


class Size(Enum):
    SMALL = 1
    s = 1
    MEDIUM  = 2
    ml =2
    LARGE = 3
    l= 3
    X_LARGE = 4
    xl =4


class Product:
    """Every product has  a name ,color and size"""

    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size


