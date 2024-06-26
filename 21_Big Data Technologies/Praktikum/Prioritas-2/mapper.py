#!/usr/bin/env python

import sys

def mapper():
    for line in sys.stdin:

        scores = line.strip().split(',')

        total_score = sum(map(float, scores))
        count = len(scores)

        print(f"{count}\t{total_score}")

if __name__ == "__main__":
    mapper()
