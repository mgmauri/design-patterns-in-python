import unittest


class Sentence:
    def __init__(self, words):
        self.words = words.split(' ')
        self.word_cases = dict()

    class WordCase:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    def __getitem__(self, index):
        item = self.WordCase()
        self.word_cases[index] = item
        return self.word_cases[index]

    def __str__(self):
        result = list()
        for index, word in enumerate(self.words):
            if index in self.word_cases and self.word_cases[index].capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return ' '.join(result)


class Evaluate(unittest.TestCase):
    def test_exercise(self):
        s = Sentence('alpha beta gamma')
        s[1].capitalize = True
        self.assertEqual(str(s), 'alpha BETA gamma')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
