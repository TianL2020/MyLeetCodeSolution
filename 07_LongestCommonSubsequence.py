# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:47:01 2021

@author: Tian


   0  0  a  c  e
   0[[0, 0, 0, 0], 
   a [0, 1, 1, 1], 
   b [0, 1, 1, 1], 
   c [0, 1, 2, 2], 
   d [0, 1, 2, 2], 
   e [0, 1, 2, 3]]
"""


class Solution(object):

    #---------------------------dynamic programming

    def longestCommonSubsequence1(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1)*len(text2)==0: return 0
        
        # initialization
        c=[[None for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        dim1,dim2=len(c), len(c[0])
        #print(dim1,dim2)

        for i in range(len(text1)+1):
            #print(i)
            c[i][0]=0
        for j in range(len(text2)+1):
            c[0][j]=0
        
        # comput the table
        for i in range(0,len(text1)):
            for j in range(0, len(text2)):
                if text1[i]==text2[j]:
                    c[i+1][j+1]=c[i][j]+1
                else:
                    c[i+1][j+1]=max(c[i][j+1],c[i+1][j])
        
        return c[len(text1)][len(text2)], c


    #------------------------------ DP faster
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
            m,n=len(text1),len(text2)
            dp=[0]*n
            res=0
            for i in range(m):
                prev=0
                for j in range(n):
                    last=dp[j]
                    if text1[i]==text2[j]:
                        dp[j]=prev+1
                    prev=max(prev,last)
                res=max(res,max(dp))
            return res

    #------------------------------ reconstruct the solution
    def getLCS(self, text1, text2, c):

        """
        two method: one to keep another table recording the directions going
        another one implemented below, has to check off diagonal first before the diagonal items
        """

        dim1,dim2=len(c), len(c[0])
        #print(dim1,dim2)

        lcs=[]

        i=dim1-1
        j=dim2-1

        while i>0 and j>0:
            #print(i, j)

            if c[i][j] == c[i-1][j]: # watch out here, has to check the off-diagonal first before checking the diagonal
                i-=1
            elif c[i][j] == c[i][j-1]:
                j-=1
            elif c[i][j] == c[i-1][j-1]+1: # when text1[i] = text2[j]
                lcs.append(text1[i-1])
                #print(lcs)
                i-=1
                j-=1

        return lcs[::-1]


sol=Solution()
s1='abcde'
s2='ace'

s1='absdjfgbhfgcde'
s2='acekjhasgddf'

n, c =sol.longestCommonSubsequence1(s1,s2)
print(n)
print('--'*20)
print(sol.getLCS(s1, s2, c))

print('--'*20)
print(sol.longestCommonSubsequence2(s1,s2))