"""
File: <histogram2.py>
Copyright (c) 2016 <Andre Perkins>
License: MIT
ENCHANCHED histogram
"""
def histogram2(pass_list):

    print" n | Data"
    print"---+----------------"

    for i in pass_list:
        st = ""

        for j in range (i):
            st = st + "*"
        print len(st),"|" , st

histogram2([4,9,13,5])
