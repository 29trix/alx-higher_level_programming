#!/usr/bin/python3
def complex_delete(my_dic, value):
    list_keys = list(my_dic.keys())

    for value_dic in list_keys:
        if value == my_dic.get(value_dic):
            del my_dic[value_dic]

    return (my_dic)
