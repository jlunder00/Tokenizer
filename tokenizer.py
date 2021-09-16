'''
Programmer: Jason Lunder
Class: CPSC 323-01, Fall 2021
Project #2 - "Tokenization"

Description: This class has the ability to tokenize a file of text into words according to specific rules: words are the characters 'I' 'A' 'a' or 2 or more alphabetical characters surrounded by non newline whitespace only. ' characters are allowed only if not at the ends of a word. This class reads a file, tokenizes it, and counts up the instances of the beginning letters of the words.
'''
from collections import Counter

class Tokenizer():

    def __init__(self, fileName):
        self.fileName = fileName
        self.read_file(fileName)

    '''
    Pre: A filename as a string indicating which file to read from
    Post: a string contianing the data in the file specified as a string
    Opens the indicated file, reads the data into the string, then closes the file before returning
    '''
    def read_file(self, fileName):
        fin = open(fileName, 'r')
        self.corpusList = fin.readlines() #read in text as a string
        fin.close()
  
    '''
    Tokenize a corpus by splitting, flattening, and filtering out unwanted strings.
    '''
    def tokenize(self):
        self.corpusList = [line for line in self.corpusList if line[0] != '\n']
        self.corpusList = [line.split(' ') for line in self.corpusList]
        self.corpusList = [[line[i] for i in range(len(line)) if i != len(line)-1] for line in self.corpusList] 
        self.corpusList = [item for line in self.corpusList for item in line if False not in [c.isalpha() or c == "'" for c in item]]
        self.corpusList = [item for item in self.corpusList if len(item) >= 2 or item == 'a' or item == 'A' or item == 'I']
        self.corpusList = [item for item in self.corpusList if item[0] != "'" and item[-1] != "'"]

    '''
    Count up the number of instances of starting letters on words in the corpus.
    '''
    def count(self):
        countList = [word[0].lower() for word in self.corpusList]
        count_of_elements = Counter(countList)
        for k, v, in count_of_elements.items():
            print(k+': '+str(v))
