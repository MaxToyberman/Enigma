from Translator import Translator


class Reflector(Translator):

    def __init__(self, permutation):
        self.reflector = list(permutation)

    def forwardTranslataion(self, letter):

        index=self.letterToIndex(letter.upper())

        return self.reflector[index]


    def reverseTranslataion(self, letter):
        return self.forwardTranslataion(letter)