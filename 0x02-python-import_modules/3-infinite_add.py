#!/usr/bin/python3
import sys
argv = sys.argv
argCount = len(argv)
res = 0
for i in range(1, argCount):
    val = int(argv[i])
    res += val
print(f"{res}")
