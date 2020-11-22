from abc import ABC
from collections.abc import Iterable
from unittest import TestCase


class Connectable(Iterable,ABC):
    def connect_to(self,other):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neurone(Connectable):

    def __init__(self,name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __iter__(self):
        yield self

    def __str__(self):
        return f"{self.name} : with {len(self.inputs)} inputs and {len(self.outputs)} outputs"


class NeuroneLayer(list,Connectable):

    def __init__(self,name:str,n_neurons_in_layer:int):
        super().__init__()
        self.name = name
        for n in range(n_neurons_in_layer):
            self.append(Neurone(f"{self.name} - {n}"))

    def __str__(self):
        return f"{self.name} has {len(self)} neurons."

if __name__ == '__main__':
    neurone1 = Neurone("N1")
    neurone2 = Neurone("N2")

    layer1 = NeuroneLayer("L1",3)
    layer2 = NeuroneLayer("L2",4)

    neurone1.connect_to(neurone2)
    neurone1.connect_to(layer1)

    layer1.connect_to(neurone2)
    layer1.connect_to(layer2)

    print(neurone1)
    print(neurone2)
    print(layer1)
    print(layer2)


class SingleValue:
    def __init__(self, value):
        self.value = value


