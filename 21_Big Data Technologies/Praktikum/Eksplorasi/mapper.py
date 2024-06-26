#!/usr/bin/env python

import sys

def is_palindrome(word):
    return word == word[::-1]

def mapper():
    for line in sys.stdin:

        words = line.strip().split()
        for word in words:

            print(f"{word}\t{is_palindrome(word)}")

if __name__ == "__main__":
    mapper()
