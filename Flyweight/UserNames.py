import random
import string
import time


def time_it(func):
    def fun():
        start:float = time.time()
        result = func()
        end:float = time.time()
        print(f"{func.__name__} took {int((end - start) * 1000)}ms")
        return result

    return fun


class User:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def random_string():
    chars = string.ascii_lowercase
    return " ".join([random.choice(chars) for _ in range(8)])


class User2:
    strings = []

    def __init__(self, name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings)-1
            
        self.names = [ get_or_add(x) for x in name.split(" ")]

    def __str__(self):
        return  " ".join([ self.strings[x]  for x in self.names ])

if __name__ == '__main__':
    users = []
    n = 10000
    first_names = [random_string() for _ in range(n)]
    last_names = [random_string() for _ in range(n)]
    # full_names = [ f"{first_name} {last_name}" for first_name,last_name in zip(first_names,last_names)]

    def check(user_class, first_names_=None, last_names_=None):
        start:float = time.time()

        print(user_class.__name__  )
        if last_names_ is None:
            last_names_ = last_names
        if first_names_ is None:
            first_names_ = first_names
        for first_name in first_names_:
            for last_name in last_names_:
                a = user_class(f"{first_name} {last_name}")
                users.append(a)
        end:float = time.time()
        print(f"{user_class} took {int((end - start) * 1000)}ms")

    check(User2)
    check(User)

