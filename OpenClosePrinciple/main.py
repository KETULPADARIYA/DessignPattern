from OpenClosePrinciple.product import Product, Color, Size
from OpenClosePrinciple.product_filters import ProductFilter, BetterFilter, ColorSpecification, \
    SizeSpecification

apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]


# old
pf = ProductFilter()
print("Green products (old):")
for p in pf.filter_by_color(products,Color.GREEN):
    print(f" - {p.name} is green")


# good and New
bf = BetterFilter()

print("Green products (new):")
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products,green):
    print(f" - {p.name} is green")


print("Large products:")
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products,large):
    print(f" - {p.size} is large")


print("Large blue items:")
large_blue = large & ColorSpecification(Color.BLUE)
for p in bf.filter(products,large_blue):
    print(f" - {p.name} is large and blue")


