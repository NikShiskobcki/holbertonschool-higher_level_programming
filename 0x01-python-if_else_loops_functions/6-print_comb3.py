#!/usr/bin/python3
for i in range(0, 10):
    for n in range(i, 10):
        if n != i:
            if i != 8 and i != 9:
                print(f"{i}{n}, ", end='')
print(f"89")
