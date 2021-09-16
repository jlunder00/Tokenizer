'''
Programmer: Jason Lunder
Class: CPSC 323-01, Fall 2021
Project #2 - "Tokenizer"

Description: This program runs the tokenizer on a given corpus 
'''
import tokenizer
import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, help='The file to tokenize', required=True)
    args = parser.parse_args()
    if args.file:
        fname = args.file
        token = tokenizer.Tokenizer(fname)
        token.tokenize()
        token.count()
    else:
        exit()

if __name__ == '__main__':
    main()
