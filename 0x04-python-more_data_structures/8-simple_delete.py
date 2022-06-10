#!/usr/bin/python3
def simple_delete(my_dic, key=""):
    if my_dic.get(key) is not None:
        del my_dic[key]
    return (my_dic)
