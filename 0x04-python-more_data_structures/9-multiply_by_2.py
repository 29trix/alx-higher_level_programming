#!/usr/bin/python3
def multiply_by_2(my_dic):

    new_dic = my_dic.copy()
    for x in new_dic.keys():
        new_dic[x] *= 2
    
    return (new_dic)
