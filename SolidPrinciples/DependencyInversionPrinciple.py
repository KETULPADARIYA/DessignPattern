from abc import abstractmethod, ABC
from enum import Enum


class Relationship(Enum):
    parent = 1
    child = 2
    sibling = 3
    Parent = 1


class RelationshipBrowser:

    @abstractmethod
    def find_all_children_of(self, name): pass


class Person:

    def __init__(self, name):
        self.name = name


class Relationships(RelationshipBrowser, ABC):

    def __init__(self):
        self.relations = []

    def add_children_parent(self, child, parent):
        self.relations.append((child, Relationship.parent, parent))
        self.relations.append((parent, Relationship.Parent, child))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.parent:
                yield r[2].name


class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_children_parent(parent, child1)
relationships.add_children_parent(parent, child2)

Research(relationships)
