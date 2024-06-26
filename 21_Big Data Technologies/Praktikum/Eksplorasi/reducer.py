#!/usr/bin/env python

import sys

def reducer():
    current_word = None
    current_count = None
    
    for line in sys.stdin:

        word, is_palindrome = line.strip().split("\t")
        
        if current_word != word:

            if current_word:
                print(f"{current_word}\t{current_count}")
            current_word = word
            current_count = is_palindrome
        else:

            current_count = current_count or is_palindrome

    if current_word:
        print(f"{current_word}\t{current_count}")

if __name__ == "__main__":
    reducer()
