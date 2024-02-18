# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, words):
        return [word for word in words if self.is_anagram(word)]

    def is_anagram(self, other_word):
        other_word = other_word.lower()
        return other_word != self.word and sorted(other_word) == self.sorted_word