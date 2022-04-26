#!/usr/bin/python3
def uppercase(str):
    x = 0
    strAux = ''

    while str[x:]:
        value = ord(str[x])
        if value > 96 and value < 123:
            strAux += chr(value - 32)
        else:
            strAux += chr(value)
        x += 1
    print(f"{strAux}")
