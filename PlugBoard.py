from Translator import Translator

'''
Author:Maxim Toyberman
Date:18.11.2015
'''
class PlugBoard(Translator):


    def __init__(self, configuration):
        '''
        :param configuration -receive a list like AB YU GH ,convert A to B Y to U G to H etc... else map each letter ti itself:
        :return:
        '''

        self.configuration = configuration.strip().split()
        self.configurationDict={}
        #self.reverseConfigurationDict={}
        for pair in self.configuration:
            self.configurationDict[pair[0]]=pair[1]
            self.configurationDict[pair[1]]=pair[0]
            #self.reverseConfigurationDict[pair[1]]=pair[0]



    def forwardTranslataion(self, letter):
        '''
        :param letter-check if letter is mapped to another letter :
        :return mapped letter if available:
        '''
        if self.configurationDict.has_key(letter):
            return self.configurationDict[letter]

        return letter.upper()


    def reverseTranslataion(self, letter):
        pass
        #if self.reverseConfigurationDict.has_key(letter):return self.reverseConfigurationDict[letter]


        #return letter.upper()

