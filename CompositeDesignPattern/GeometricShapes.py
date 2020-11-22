
class GraphicObject:

    def __init__(self ,color=None):
        self.color =color
        self.colors = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    def collect_str(self, container: list, n_instances: int or float):
        # print **ColorName
        container.append("*" * n_instances)
        if self.color:
            container.append(self.color)
        container.append(f"{self.name}\n")
        # put children in container
        for color in self.colors:
            color.collect_str(container, n_instances + 1)

    def __str__(self):
        a = []
        self.collect_str(a, 0)
        return " ".join(a)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = "My Drawing"
    drawing.colors.append(Circle("Red"))
    drawing.colors.append(Circle("Yellow"))

    group = GraphicObject()
    group.colors.append(Circle("Blue"))
    group.colors.append(Circle("NavyBlue"))

    drawing.colors.append(group)
    print(drawing)