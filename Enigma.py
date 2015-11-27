
from Substitutor import Substitutor
'''
Author:Maxim Toyberman
Date:18.11.2015
'''

class Enigma(Substitutor):

    def __init__(self, rotors, reflector, plugBoard):

        """
        :param rotors: rotors[2]-rightmost rotor, rotors[1]-middle rotor,rotors[0]-leftmost rotor
        :param reflector-the reflector used in the machine:
        :param plugBoard-plugboard used by the machine :
        :return:
        """
        self.rotors = rotors
        self.reflector = reflector
        self.plugBoard = plugBoard

    def moveRotors(self):
        '''
                this method handles the rotors movement (considering the turnovernotch)
        '''
        if self.rotors[2].IsTurnOverNotch() or self.rotors[1].IsTurnOverNotch():
            if self.rotors[1].IsTurnOverNotch():
                self.rotors[0].advanceOffSet()
            self.rotors[1].advanceOffSet()
        self.rotors[2].advanceOffSet()


    def encryptDecrypt(self, word):
        '''

        :param word-received to encrypt/decrypt:
        :return:encrypted/decrypted word
        '''
        encrypted=""

        for letter in word:
            #at first we move the rotors
            self.moveRotors()
            #the user press a key and it goes through the plugboard
            translatedLetter = self.plugBoard.forwardTranslataion(letter.upper())

            #R-M-L - the letter moves through the rotors and is being encrypted on every rotor
            first=self.rotors[2].encryptedLetter(translatedLetter)
            second=self.rotors[1].encryptedLetter(self.toChar(first))
            third=self.rotors[0].encryptedLetter(self.toChar(second))

            #after the rotor the letter goes through the reflector
            reflected= self.reflector.forwardTranslataion(self.toChar(third))
            #L-M-R - the letter from the reflector is going throuh the rotors again but the other direction , and the operation is in reverse direction (reverse permutation)
            first=self.rotors[0].decryptLetter(reflected)

            second=self.rotors[1].decryptLetter(self.toChar(first))
            third=self.rotors[2].decryptLetter(self.toChar(second))
            #the letter goes through the plugboard again
            translatedLetter = self.plugBoard.forwardTranslataion(self.toChar(third))
            #adding encrypted letter to the word
            encrypted+=translatedLetter
        return  encrypted


    def toChar(self,number):
        '''
        :param number:
        :return converted number to a character:
        '''
        return chr(ord('A')+number)

    def forwardTranslataion(self,permutation):
        pass

    def reverseTranslataion(self, permutation):
        pass
