from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:

    # def __init__(self,x,y):
    #     self.x = x
    #     self.y = y

    def __str__(self):
        return f"x: {self.x}, y :{self.y}"

    # redeclaration won't work

    # def __init__(self,rho,theta):

    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b

        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)


    # steps to add a new system
    # 1. augment CoordinateSystem
    # 2. change init method

    @staticmethod
    def new_cartesian_pont(x,y):
        return  Point(x,y)

    @staticmethod
    def new_polar_point(x,y):
        return Point(x * sin(y), y * cos(x))

    class Factory:
        @staticmethod
        def new_cartesian_point(x,y):
            return Point(x,y)

    factory = Factory()