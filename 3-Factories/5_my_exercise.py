class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    def __init__(self):
        self.count = 0

    def create_person(self, name):
        self.person = Person(self.count, name)
        self.count += 1
        return self.person
