#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for list in range(x):
            print("{}".format(my_list[list]), end="")
        print("")
    except:
        print("")
        return list
    return x

