#!/usr/bin/env python3

from collections import Counter
import sys

def hex_conv(test):
    yo = test.encode("utf-8")
    te = yo.hex()
    li = [(i+j) for (i,j) in zip(te[::2],te[1::2])]
    return li

test = sys.argv[1]
f = open(test,"r")
sum=''
for row in f:
    sum+=row

print(hex_conv(sum))
