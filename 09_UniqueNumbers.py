# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:17:23 2021

@author: Tian


input: [1,1,1,3,1,3,3,3,2,2]
output: [1, 3, 2]
get the unique numbers in the list that is in the order they presented

use set as seen, O(n)

"""

my_list= [1,1,1,3,1,3,3,3,2,2]

def get_uniquenumber(lst):

    que=[]
    seen = set() # use the set for seach in O(1)
    for i in range(len(lst)):
        if lst[i] not in seen:
            que.append(lst[i])
            seen.add(lst[i])

    return que

print(get_uniquenumber(my_list))

