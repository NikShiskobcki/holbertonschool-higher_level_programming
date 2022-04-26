#!/usr/bin/python3
x = 122
y = 89
while x >= 97:
    print(f"{chr(x)}{chr(y)}", end='')
    x -= 2
    y -= 2
