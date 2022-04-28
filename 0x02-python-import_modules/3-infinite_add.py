#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argCount = len(argv)
    res = 0
    for i in range(1, argCount):
        val = int(argv[i])
        res += val
    print(f"{res}")
