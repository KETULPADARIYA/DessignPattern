class Manager:

    def __init__(self):
        self.developers = []
        self.designers = []
        self.testers = []

    def add_developer(self, devloper):
        self.developers.append(devloper)

    def add_designer(self, designer):
        self.designers.append(designer)

    def add_tester(self, tester):
        self.testers.append(tester)


class Developer:

    def __init__(self):
        print("developer added")


class Designer:

    def __init__(self):
        print("Designer added")


class Tester:

    def __init__(self):
        print("tester added")


if __name__ == '__main__':
    a = Manager()
    a.add_developer(Developer())
    a.add_designer(Designer())

    print("problem is that not quality assurance is new department so what we will do ")
