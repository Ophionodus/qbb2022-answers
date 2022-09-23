#!/usr/bin/env python
import sys


    
differences = 0
    
try:
    file1 = open(sys.argv[1], "b")
except:
    print("file1wontopen")
try:
    file2 = open(sys.argv[2], "b")
except:
    print("file2wontopen")





for line in file1:
    if ([*file1[line]]) != ([*file2[line]]):
        differences = differences + 1

print(file1)
print(file2)
print(differences)