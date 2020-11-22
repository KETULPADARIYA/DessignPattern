class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        # TODO
        self.width = square.side
        self.height = square.side

if __name__ == '__main__':
    sq = Square(12)
    print(calculate_area(SquareToRectangleAdapter(sq)))