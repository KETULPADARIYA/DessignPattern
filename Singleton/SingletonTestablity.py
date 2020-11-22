import unittest


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        f = open("capitals")
        lines = f.readlines()
        liners_iter = iter(lines)
        for i in liners_iter:
            self.population[i.strip()] = int(next(liners_iter).strip().replace(",", ""))

        f.close()


class SingletonRecordFinder:

    @staticmethod
    def total_population(cities):
        return sum(Database().population[city] for city in cities)


class ConfiguredSingletonRecordFinder:

    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        return sum(self.db().population[city] for city in cities)


class DummyDatabase(metaclass=Singleton):
    population = {
        "alpha": 1,
        "beta": 2,
        "gamma": 3
    }

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ["DELHI", "DHAKA"]
        tp = rf.total_population(names)
        self.assertEqual(25578000, tp)

    ddb = DummyDatabase

    def test_dependent_total_population(self):
        crf = ConfiguredSingletonRecordFinder(self.ddb)
        self.assertEqual(3,crf.total_population(["alpha","beta"]))

if __name__ == '__main__':
    unittest.main()
