from Translator import Translator

'''
Author:Maxim Toyberman
Date:18.11.2015
'''

class Rotor(Translator):
    def __init__(self, ringOffset, ringSetting, permutation, notch):
        super(self.__class__, self).__init__(permutation)
        self.ringOffset = ringOffset
        self.ringSetting = ringSetting
        self.notch = notch

    def encryptedLetter(self, letter):
        '''
        using the formula P(A+B+C)-B+C
        :param letter-receiving plain text letter and convert it to cipher text:
        :return: cipher text letter
        '''

        rightShifted = self.rightCircularShift(self.letterToIndex(letter),self.ringOffset-1)
        print( chr(ord('A')+rightShifted));
        leftShifted = self.leftCircularShift(rightShifted,self.ringSetting - 1)
        translated = self.forwardTranslataion(chr(ord('A')+leftShifted))
        result = self.rightCircularShift(self.letterToIndex(translated), self.ringSetting - 1 - (self.ringOffset - 1))

        return result

    def decryptLetter(self, letter):
        '''
        using the formula P(A+B+C)-B+C
        :param letter-receiving cipher text letter and convert it to plain text:  (the only difference is the direction (forward or reverse permutation)
        :return: cipher text letter
        '''
        rightShifted = self.rightCircularShift(self.letterToIndex(letter),self.ringOffset-1)
        leftShifted = self.leftCircularShift(rightShifted,self.ringSetting - 1)
        translated = self.reverseTranslataion(chr(ord('A')+leftShifted))
        result = self.rightCircularShift(self.letterToIndex(translated), self.ringSetting - 1 - (self.ringOffset - 1))

        return result

    def IsTurnOverNotch(self):
        return self.ringOffset == self.notch

    def advanceOffSet(self):
        #advance rotor by one each key press
        self.ringOffset=self.rightCircularShift(self.ringOffset,1)

