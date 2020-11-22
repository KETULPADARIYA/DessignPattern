class Translate:

    def __init__(self, translations_d):
        self.translations = translations_d

    def localise(self, msg):
        return self.translations.get(msg, msg)


class FrenchLocalise(Translate):
    """ translate english to French"""

    def __init__(self):
        translations_d = {"car": "voiture",
                          "bike": "bicicleta",
                          "cycle": "ciclo"}
        super().__init__(translations_d)


class SpanishLocalise(Translate):
    """ translate english to Spanish"""

    def __init__(self):
        translations_d = {"car": "coche", "bike": "bicicleta",
                          "cycle": "ciclo"}
        super().__init__(translations_d)


class EnglishLocalise(Translate):
    def __init__(self):
        translations_d = {}
        super().__init__(translations_d)


def Factory(language):
    """Factory Method"""
    localizes = {
        "French": FrenchLocalise,
        "English": EnglishLocalise,
        "Spanish": SpanishLocalise
    }

    return localizes[language]()


if __name__ == '__main__':
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")
    message = ["car", "bike", "cycle"]

    for msg in message:
        print(msg, "in french", f.localise(msg))
        print(msg, "in english", e.localise(msg))
        print(msg, "in spanish", s.localise(msg))
        print()
