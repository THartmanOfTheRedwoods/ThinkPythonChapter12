#!/usr/bin/env python3

import unicodedata  # Imported unicodedata so I could find punctuation marks (unicodedata.category that startswith 'P')

def get_punctuation(filename):
    punc_marks = {}
    with open(filename) as fp:
        for line in fp:
            for char in line:
                category = unicodedata.category( char )
                if category.startswith( 'P' ):
                    punc_marks[char] = 1
    return ''.join(punc_marks)

def split_line(line):
    return line.replace('—', ' ').split()

def clean_word(word, punctuation):
    return word.strip(punctuation).lower()

def process_word_trigram(word, window, trigram_counter):
    window.append( word )
    if len(window) == 3:
        count_trigram(window, trigram_counter)
        window.pop(0)  # Shift the window by removing the first element.

def count_trigram(trigram, trigram_counter):
    key = tuple(trigram)
    trigram_counter[key] = trigram_counter.get(key, 0) + 1

def find_max(counter):
    v_max = 0
    max_key = None
    for k,v in counter.items():
        if v > v_max:
            v_max = v
            max_key = k
    return max_key, counter[max_key]

def find_max_v2(counter):
    max_key = sorted(counter, key=lambda key: counter[key])[-1]
    return max_key, counter[max_key]

def find_max_v3(counter):
    max_key =max(counter, key=lambda key: counter[key])
    return max_key, counter[max_key]

def main():
    file_path = 'files/dr_jekyll_and_mr_hyde.txt'
    window = []
    trigram_counter = {}
    punctuation = get_punctuation(file_path)

    with open(file_path, 'r') as fp:
        for line in fp:
            for word in line.split():
                word = clean_word(word, punctuation)
                process_word_trigram(word, window, trigram_counter)

    print(find_max(trigram_counter))
    print(find_max_v2(trigram_counter))
    print(find_max_v3(trigram_counter))


if __name__ == '__main__':
    main()