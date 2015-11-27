from Enigma import Enigma
from PlugBoard import PlugBoard
from Reflector import Reflector
from Rotor import Rotor
import time





#5 default Rotors
rotor1 = Rotor(6,1,"EKMFLGDQVZNTOWYHXUSPAIBRCJ",17)
rotor2 = Rotor(4,1,"AJDKSIRUXBLHWTMCQGZNPYFVOE",5)
rotor3 = Rotor(22,1,"BDFHJLCPRTXVZNYEIWGAKMUSQO",22)
rotor4 = Rotor(18,24,"ESOVPZJAYQUIRHXLNFTGKDCMWB",10)
rotor5 = Rotor(15,9,"VZBRGITYUPSDNHLXAWMJQOFECK",26)

#1 default Reflector
reflecor=Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
#default plugBoard configuration
plugboard=PlugBoard("")
#rotors chosen for the Enigma machine
rotors=[rotor1,rotor2,rotor3]
#creating the Enigma Machine
machine=Enigma(rotors,reflecor,plugboard)

#encryption/decryption of the word
start_time = time.time()
res=""

res=machine.encryptDecrypt("DHTYYZHUCNHUTQ")

print("The encrypted word is:"+ res)




