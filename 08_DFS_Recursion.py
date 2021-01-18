# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:01:28 2021

@author: Tian

DFS Recursion

use recursion to record the use of + and - for each layer

1. You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
Find out how many ways to assign symbols to make sum of integers equal to target S.
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5         
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

res = 0  -> res  + nums[0] -> res  + nums[0] + nums[1] == S      cnt+1
			      -> res  + nums[0] - nums[1]  != S       cnt
      res  - nums[0] -> res  - nums[0] + nums[1] == S      cnt+1
      ->res  - nums[0] - nums[1] == S      cnt+1

"""

res_ct=0

def get_numways(lst, s):

    cal_val(lst,s,0, 0)

    return  res_ct


def cal_val(lst, s, num_layer, summation):

    global res_ct

    if num_layer == len(lst):

        if summation == s:
            res_ct += 1
        return

    sum1=summation
    sum1+=lst[num_layer]
    cal_val(lst, s, num_layer+1, sum1)

    sum2=summation
    sum2-=lst[num_layer]
    cal_val(lst, s, num_layer+1, sum2)


my_list = [1, 1, 1, 1, 1]
s = 3
print(get_numways(my_list, s))