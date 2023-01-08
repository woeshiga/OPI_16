#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def del_number(types='even'):
    def helper(lst):
        if types == 'even':
            lst = [i for i in lst if i % 2 != 0]
        else:
            lst = [i for i in lst if i % 2 == 0]
        return lst

    return helper
