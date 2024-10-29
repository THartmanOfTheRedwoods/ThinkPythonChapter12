#!/usr/bin/env python3

from random import choice
from Excercise02 import get_punctuation, split_line, clean_word
from Excercise03 import load_successor_map, add_trigram

def main():
    # file_path = 'files/half_a_bee.txt'
    file_path = 'files/dr_jekyll_and_mr_hyde.txt'
    window = []
    successor_map = {}
    punctuation = get_punctuation( file_path )
    load_successor_map(file_path, window, successor_map)
    successors = list(successor_map)
    bigram = choice(successors)

    line = ''
    for i in range(50):
        next_words = successor_map[bigram]
        word = choice(list(next_words))
        line += ' ' + word
        if len(line) >= 75:
            print(line)
            line = ''
        bigram = (bigram[1], word)


if __name__ == '__main__':
    main()