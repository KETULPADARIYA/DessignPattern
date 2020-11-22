class Journal:

    def __init__(self):
        self.text = ""
        self.next = 0
        self.journal = []

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def add_to_journal(self, value):
        self.text = value
        self.journal.append(self.text)

    def read_journal(self):
        for n, text in enumerate(self.journal):
            print(n, text)

    def remove_entry(self, pos):
        del self.journal[pos]

    def __str__(self):
        return "\n".join(self.journal)


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))


journel = Journal()
journel.add_to_journal("Today is horrible day")
print(journel.text)
journel.add_to_journal("Today is Good day")
print(journel.text)
journel.read_journal()
