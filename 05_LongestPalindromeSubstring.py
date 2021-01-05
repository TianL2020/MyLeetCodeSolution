# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 13:39:09 2021

@author: Tian

Longest Palindrome Substring

https://leetcode.com/problems/longest-palindromic-substring/solution/

"""


class Solution(object):

    #------------------------------Dynamic programming solution
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        #create the table
        p=[[False for i in range(len(s))] for j in range (len(s))]
    
        # initialization
        for i in range(len(s)):
            p[i][i]=True
    
        max_len=1
        start=0
        end=0
        for r in range(len(s)):
            for l in range(r-1, -1, -1):
    
                if s[r]==s[l] and (r-l<3 or p[l][r] or p[l+1][r-1]):
                    p[l][r]= True
                    if r-l+1 > max_len:
                        max_len=r-l+1
                        start=l
                        end=r
    
        return s[start : end+1]

    # notice the solution below fails the "abcba" case, have to fix the r
    # and move l from r-1 to 0 to avoid the failure (see the code above)

    def longestPalindrome2(self,s):

        #create the table
        p=[[False for i in range(len(s))] for j in range (len(s))]

        # initialization
        for i in range(len(s)):
            p[i][i]=True

        max_len=1
        start=0
        end=0
        for i in range(len(s)):
            for j in range(i+1, len(s)):

                if s[j]==s[i] and (j-i<3 or p[i][j-1]):
                    p[i][j]= True
                    if j-i+1 > max_len:
                        max_len=j-i+1
                        start=i
                        end=j

        return s[start : end+1]


    # Optimal
    #------------------------------expand around the center, where the center could be at char or in between
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1: return s
        
        if len(s)==2: return s if s[0]==s[1] else s[0]
                
        #len(s)>3
        #max_len=1

        ans=(1,0,0)
        i=0
        while i< len(s):
            ans1=self.expand(s,i,i)
            ans2=self.expand(s,i,i+1)

            if ans1[0]>ans2[0]:
                ans0=ans1
            else:
                ans0=ans2

            step=1
            if ans0[0]>ans[0]:
                ans=ans0
                step=ans[0]//2
            i+=step

        return s[ans[1]:ans[2]+1]


    def expand(self, s,l,r):
        ans=(1,l,r)
        while l>=0 and r< len(s):

            if s[l]==s[r]:
                ans=(r-l+1,l,r)

                l-=1
                r+=1
            else:
                break

        return ans


sol=Solution()
s='cbbd'
s='aaaa'
s='abcba'

print(sol.longestPalindrome(s))
print(sol.longestPalindrome1(s))
print(sol.longestPalindrome2(s))