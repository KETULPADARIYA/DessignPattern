class CEO:
    # static variable starts with __
    __shared_state = {
        "name": "Steve",
        "age": 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class MonoState:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(MonoState, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(MonoState):

    def __init__(self):
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages ${self.money_managed}"


if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 77
    print(ceo1)
    print(ceo2)

    cfo1 = CFO()
    cfo1.name = "charles"
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = "ruthles"
    cfo2.money_managed = 1000
    print(cfo1,f"\n{cfo2}")
