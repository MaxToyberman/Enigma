from Substitutor import Substitutor


class Translator(Substitutor):


    def __init__(self,permutation):
        self.permutation=list(permutation.upper())

    def forwardTranslataion(self,letter):

        return self.permutation[self.letterToIndex(letter)]

    def reverseTranslataion(self, letter):

        return chr(ord('A')+self.permutation.index(letter.upper()))
