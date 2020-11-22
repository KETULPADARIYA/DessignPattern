import copy


class Address:

    def __init__(self, street_address, suite, country):
        self.suite = suite
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f"{self.street_address}, Suite #{self.suite}, {self.country}"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", "Suite #101", "London"))
    aux_office_employee = Employee("", Address("123b East Dr", "Suite #101", "London"))



    @staticmethod
    def __new_employee(proto, name, suite):
        em = copy.deepcopy(proto)
        em.name = name
        em.address.suite = suite
        return em

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee,
                                              name, suite)

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee,
                                              name, suite)


john = EmployeeFactory.new_main_office_employee("John", "102")
jane = EmployeeFactory.new_aux_office_employee("Jane", "421")

print(john)
print(jane)