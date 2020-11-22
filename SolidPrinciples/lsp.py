class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'Width :{self.width} Height : {self.height}'


class Square(Rectangle):

    def __init__(self, size: int):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, size):
        self._width = self._height = size

    @Rectangle.height.setter
    def height(self, size):
        self._width = self._height = size


def Use_it(rc):
    w = rc.width

    rc.height = 10  # unpleasant side effect
    expected = int(w*10)
    print( F"expected result is {expected} but got is {rc.area()}")

rc = Rectangle(3,5)
Use_it(rc)


rc = Square(5)
Use_it(rc)