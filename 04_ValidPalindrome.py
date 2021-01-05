# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:03:11 2021

@author: Tian

Valid Palindrome


"""


class Solution(object):

    # comparing to its inverse
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_lower=s.lower()
        
        clst=[]
        
        for c in s_lower:
            if c.isalpha() or c.isnumeric():
                clst.append(c)
        
        i=0
        j=len(clst)-1
        while i <j:
            if clst[i]!=clst[j]:
                return False
            else:
                i+=1
                j-=1
        return True

     # using two pointer method
    def isPalindrome2(self,s):

        l=0
        r=len(s)-1

        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1

            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1

        return True

sol=Solution()
s='kasjdfghkjhg'
print(sol.isPalindrome(s))
print(sol.isPalindrome2(s))