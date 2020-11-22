import copy
from abc import ABCMeta, abstractmethod


class Course(metaclass=ABCMeta):

    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class DSA(Course):
    def __init__(self):
        super().__init__()
        self.type = "DATA structure and Algorithm"

    def course(self):
        print("Inside the DSA::course() method")


class SDE(Course):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"

    def course(self):
        print("Inside the DSA::course() method")


class CoursesAtUni:
    cache = {}

    @staticmethod
    def get_course(sid):
        Course = CoursesAtUni.cache.get(sid, None)
        return Course.clone()

    @staticmethod
    def load():
        sde = SDE()
        sde.set_id("1")
        CoursesAtUni.cache[sde.get_id()] = sde

        dsa = DSA()
        dsa.set_id("2")
        CoursesAtUni.cache[dsa.get_id()] = dsa

if __name__ == '__main__':
    CoursesAtUni.load()

    sde = CoursesAtUni.get_course("1")
    print(sde.get_type())

    dsa = CoursesAtUni.get_course("2")
    print(dsa.get_type())
