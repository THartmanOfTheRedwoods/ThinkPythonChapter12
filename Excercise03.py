#!/usr/bin/env python3

from pprint import pprint  # For pretty-printing my successor map
from string import punctuation

from Excercise02 import get_punctuation, split_line, clean_word

def process_word_trigram(word, window, successor_map):
    window.append( word )
    if len(window) == 3:
        add_trigram(window, successor_map)
        window.pop(0)  # Shift the window by removing the first element.

def add_trigram(trigram, successor_map):
    first, second, third = trigram
    key = (first, second)
    successor_map.setdefault((first, second), set()).add(third)

def load_successor_map(file_path, window, successor_map):
    punctuation = get_punctuation(file_path)
    with open(file_path, 'r') as fp:
        for line in fp:
            for word in line.split():
                word = clean_word(word, punctuation)
                process_word_trigram(word, window, successor_map)

def main():
    file_path = 'files/dr_jekyll_and_mr_hyde.txt'
    # file_path = 'files/half_a_bee.txt'
    window = []
    successor_map = {}
    load_successor_map(file_path, window, successor_map)
    pprint(successor_map, indent=4)

if __name__ == '__main__':
    main()