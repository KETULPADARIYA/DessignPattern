class Word:
    def __init__(self, word):
        self.word = word
        # self.index = index

        self._capitalize = True if word.isupper() else False

    @property
    def capitalize(self):
        return self._capitalize

    @capitalize.setter
    def capitalize(self, value):
        self._capitalize = value
        if value:
            self.word = self.word.upper()

    def __str__(self):
        return self.word


class Sentence:

    def __init__(self, plain_text):
        # todo
        self.tokens = plain_text.split()
        self.words = [Word(token) for token in self.tokens]

    def __getitem__(self, item):
        return self.words[item]

    def __str__(self):
        return " ".join(str(word) for word in self.words)


if __name__ == '__main__':
    sentence = Sentence("hello world")
    sentence[0].capitalize = True
    print(sentence)
