from random import random, choice


class DSA:
    """Class for Data Structure and Algorithms"""
    def Fee(self):
        return  11000

    def __str__(self):
        return "DSA"


class STL:
    """Class for Standard Template Library"""

    def Fee(self):
        return 7000

    def __str__(self):
        return "STL"


class SDE:
    """Class for Software Developer Engineer Course"""

    def Fee(self):
        return 15000

    def __str__(self):
        return "SDE"


class CourseFactory:

    def __init__(self,course_factory):
        if isinstance(course_factory,str):
            self.course_factory = eval(course_factory)()


    def info(self):

        print(f"Course Name is {self.course_factory}")
        print(f"fee is {self.course_factory.Fee()}\n")


def random_select_course():
    """choose random course"""
    return choice(["STL","SDE","DSA"])


if __name__ == '__main__':
    for i in range(5):
        CourseFactory(random_select_course()).info()