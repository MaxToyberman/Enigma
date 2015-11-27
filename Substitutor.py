from abc import ABCMeta, abstractmethod


# abstract class Substitutor
class Substitutor:
    __metaclass__ = ABCMeta

    num_of_letters = 26

    @abstractmethod
    def forwardTranslataion(self,permutation):
        pass

    @abstractmethod
    def reverseTranslataion(self, permutation):
        pass

    def letterToIndex(self, letter):
        return ord(letter.upper()) - ord('A')

    def leftCircularShift(self, letter, numOfShifts):
        return self.rightCircularShift(letter,26-numOfShifts)

    def rightCircularShift(self, letter, numOfShifts):
        if (numOfShifts<0):
            return  (letter+26+numOfShifts)%26
        return (letter + numOfShifts) % 26
