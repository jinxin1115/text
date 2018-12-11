# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:46:31 2018

@author: Administrator
"""
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)
