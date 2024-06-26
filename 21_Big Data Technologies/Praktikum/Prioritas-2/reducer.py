#!/usr/bin/env python

import sys

def reducer():
    total_count = 0
    total_score = 0
    
    for line in sys.stdin:

        count, score = map(float, line.strip().split('\t'))

        total_count += count
        total_score += score

    average_score = total_score / total_count
    print(f"Rata-rata\t{average_score}")

if __name__ == "__main__":
    reducer()
