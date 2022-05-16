#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for list in range(x):
            print(f"{my_list[list]}", end="")
        print("")
    except (ValueError, TypeError, IndexError):
        print("")
        return list
    return x
