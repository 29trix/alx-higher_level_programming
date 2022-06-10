#!/usr/bin/python3
def multiply_by_2(my_dic):
    new_dir = my_dic.copy()
    list_keys = list(new_dic.keys())

    for i in list_keys:
        new_dic[i] *= 2

    return (new_dic)
