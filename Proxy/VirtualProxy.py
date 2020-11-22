class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print("drawing the file")


class LazyBitmap:

    def __init__(self, filename):
        self.filename = filename
        self._bit_map = None

    def draw(self):
        if self._bit_map is None:
            self._bit_map = Bitmap(self.filename)
        self._bit_map.draw()


if __name__ == '__main__':
    b = Bitmap("123.png")
    b.draw()
    b = Bitmap("123.png")


    print("\n ---- Lazy Bitmap ----\n")
    l = LazyBitmap("123.png")

    l.draw()

    l = LazyBitmap("123.png")

