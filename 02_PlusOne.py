# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:54:18 2021

@author: Tian

PlusOne

https://leetcode.com/explore/featured/card/google/59/array-and-strings/339/

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res=[]
        if digits[-1]<9: # if last digit is less than 9
            res=digits[:]
            res[-1]+=1
            return res
        
        else:
            found=False
            for i in range(len(digits)-1,-1,-1):
                if digits[i]!=9:
                    found= True
                    break

            if not found: #not found
                res=[0 for i in range(len(digits))]
                res.insert(0,1)
            else:
                res=digits[:]
                res[i]+=1
                for j in range(i+1, len(digits)):
                    res[j]=0
            return res

sol=Solution()
digit=[9]
print(sol.plusOne(digit))

