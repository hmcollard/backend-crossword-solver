#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Haley Collard"

import re


def make_dict():
    word_dict = {}
    with open("dictionary.txt", 'r') as f:
        words = f.read().split()
        for word in words:
            l = len(word)
            word_dict.setdefault(l, [])
            word_dict[l].append(word)
    return word_dict


def main():
    word_dict = make_dict()

    test_word = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
    re_word = test_word.replace(' ', '\S')
    # re_search_word = f'{re_word}'
    word_length = len(test_word)
    possible_word_matches = []
    for word in word_dict[word_length]:
        match = re.search(re_word, word)
        if match:
            possible_word_matches.append(match.string)

    print(possible_word_matches)

    # raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()
