#!/usr/bin/env python3
#cording = utf-8

import binascii
import sys
import subprocess
import difflib
import shlex

#diffrent calculation fanction
def diff(f1,f2):
    d = difflib.Differ()
    s = "\n".join(d.compare([f1],[f2]))
    return s
#diffirent %
def difnumber(x,y):
    di = difflib.SequenceMatcher(None, f1,f2).ratio()
    return di
## it is specify here, file convert hex and binascii, very easy program

file1 = shlex.split("hexdump -C file1")
file2 =shlex.split("hexdump -C file2")
f1 = subprocess.check_output(file1).decode("UTF-8").strip()
f2 = subprocess.check_output(file2).decode("UTF-8").strip()
diff = diff(f1,f2)
diffnum = difnumber(f1,f2)
#with open("file_hex.txt",w) as f:
#    print()
print(diff);
print("match:{}".format(diffnum))
