"""Word Finder: finds random words from a dictionary."""
import os
import random
class WordFinder:
    ...
    def __init__(self):
        """ wordlist = empty wordlist then adds all the words in from words.txt"""
        self.wordlist = []
        file = open("coding/Python/python-oo-practice/words.txt")
        for line in file:
          self.wordlist.append(line)
        file.close()
    def random(self):
        """returns a random word from the wordlist, then strips off newline with rstrip
        """
        return self.wordlist[random.randint(0, len(self.wordlist))].rstrip()
    def SpecialwordFinder(self):
        not_vaild = True
        temp_word = self.random()
        while not_vaild:
            if temp_word[0] == '#' or temp_word == '\n':
                temp_word = self.random()
            else:
                return temp_word

wordObj = WordFinder()
print(wordObj.random())
#print(os.getcwd())