#3.35
#write a function that returns the number of occurrences of
#a pair of character in a dna string
#for example , calling the function dna as ACTGGCTATCCATT
#and a pair as 'at' will return 2.

"""
File: count_pairs.py
Copyright (c) 2016 Andre Perkins
License: MIT
Shows how many time AT shows up, I gave up on the user_input lol
"""

def count_v2(dna,pair):
    i = 0
    for AT in dna:
        if AT == pair:
            i += 1
    return dna.count(pair)

dna = 'ACTGGCTATCCATT'
pair = "AT"
n = count_v2(dna,pair)
print '%s appears %d times in %s' % (pair,n, dna)
