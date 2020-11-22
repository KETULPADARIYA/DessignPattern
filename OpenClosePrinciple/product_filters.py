class ProductFilter:
    """ Hard to maintain and violate OCP and SRP so hard to test """

    def filter_by_color(self,  products,color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, product, size):
        for p in product:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, product, size, color):
        for p in product:
            if p.size == size and p.color == color:
                yield p
    # state space explosion
    # 3 criteria
    # c s w cs sw cw csw = 7 methods

    # OCP = open for extension, closed for modification


class Specification:

    def is_satisfied(self, item):
        pass

    def __add__(self, other):
        return AndSpecification(self, other)


class Filter:

    def filter(self, item, spec):
        pass


class ColorSpecification(Specification):

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):

    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
