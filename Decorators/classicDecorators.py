from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ""


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"Circle(r = {self.radius})"


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"Square(side = {self.side})"


class ColoredShape(Shape):
    def __init__(self,shape,color):
        if isinstance(shape,ColoredShape):
            raise Exception("Cannot apply same decorator twice")
        self.color = color
        self.shape = shape

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


class TransparentShape(Shape):
    def __init__(self,shape,transparency):
        self.shape = shape
        self.transparency =transparency

    def __str__(self):
        return f"{self.shape} is a {self.transparency*100.0}% transparent."


if __name__ == '__main__':
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape("Red",circle)
    print(red_circle)
    try:
        red_circle.resize(2)
    except AttributeError as e:
        print(e)

    red_half_transparent = TransparentShape(red_circle,0.5)
    print(red_half_transparent)

    try:
        print(ColoredShape(ColoredShape(circle,"Red"),"green"))
    except Exception as e:
        print(e)