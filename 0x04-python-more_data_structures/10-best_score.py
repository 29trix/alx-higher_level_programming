#!/usr/bin/python3
def best_score(my_dic):
    if not my_dic:
        return (None)

    return (max(my_dic, key=my_dic.get))
