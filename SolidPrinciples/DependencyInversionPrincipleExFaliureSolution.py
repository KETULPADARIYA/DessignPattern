from abc import abstractmethod


class Employee:
    @abstractmethod
    def Work(self):
        pass


class Manager:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


class Developer(Employee):

    def __init__(self):
        print("Developer is added")

    def Work(self):
        print("Developer is working")


class Designer(Employee):

    def __init__(self):
        print("Designer is added")

    def Work(self):
        print("Designer is working")


class Tester(Employee):

    def __init__(self):
        print("Tester is added")

    def Work(self):
        print("Tester is working")


if __name__ == "__main__":
    a = Manager()
    a.add_employee(Developer())
    a.add_employee(Designer())
