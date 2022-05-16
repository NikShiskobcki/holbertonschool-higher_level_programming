#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    aux = []
    for x in range(list_length):
        div = 0
        try:
            div = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            aux.append(div)
    return aux
