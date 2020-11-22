class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


def verify_age(person, age_limit, method):
    return "too young" if person.age < age_limit else method


class ResponsiblePerson:

    def __init__(self, person):
        self.person = person
        if isinstance(person, str):
            self.person = Person(person)

    @property
    def age(self):
        return self.person.age

    @age.setter
    def age(self, value):
        self.person.age = value

    # todo: rest of this class


def drink(self):
    return verify_age(self.person, 18, self.person.drink)


def drive(self):
    return verify_age(self.person, 16, self.person.drive)


def drink_and_drive(self):
    return "dead"