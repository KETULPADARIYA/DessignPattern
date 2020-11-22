from abc import abstractmethod


class Machine:

    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


class MultiFunctionPrinter(Machine):

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class Printer:

    @abstractmethod
    def print(self, document):
        pass


class Scanner:

    @abstractmethod
    def scan(self, document):
        pass


# same for Fax, etc.
class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):

    def print(self, document):
        print(document)

    def scan(self, document):
        print(document)


class MultiFunctionDevice(Printer, Scanner):  # ,Fax, etc

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):

    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


if __name__ == '__main__':
    printer = OldFashionedPrinter()
    printer.fax(123)
    printer.scan(123)
    printer.print(123)