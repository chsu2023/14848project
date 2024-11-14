#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

# Read input from standard input
for line in sys.stdin:
    # Remove leading/trailing whitespace
    line = line.strip()
    # Parse input from mapper
    word, count = line.split('\t')
    count = int(count)
    
    # Check if the word is the same as the previous word
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Output the word and its count
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Output the last word and its count
if current_word:
    print(f"{current_word}\t{current_count}")