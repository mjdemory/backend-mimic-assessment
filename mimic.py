#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Michael DeMory and received help from Mimic video done by Daniel, Tiffany McLean"

import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    mimic_dict = {}

    with open(filename, 'r') as f:
        contents = f.read ()
        words = contents.split()
        mimic_dict[''] = [words[0]]
    i = 0
    for i in range (len(words) - 1):
        if words[i] not in mimic_dict:
            mimic_dict[words[i]] = [words[i + 1]]
        else:
            mimic_dict[words[i]].append(words[i+1])
        i += 1
    return mimic_dict


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    mimic_words = []
    while len(mimic_words) <= 200:
        if start_word in mimic_dict:
            next_word = random.choice(mimic_dict[start_word])
            mimic_words.append(next_word)
            start_word = next_word
        else:
            start_word = ''
    print (' '.join(mimic_words))
    


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')
    


if __name__ == '__main__':
    main()
