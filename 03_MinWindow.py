# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 22:18:09 2021

@author: Tian

minWindow

Sliding window method to find the min window containing the desired str

https://leetcode.com/problems/minimum-window-substring/solution/

"""

from collections import Counter
import time

class Solution(object):

    #-------------------------------------------sliding window
    # check for each small window that contains only 1 set of target t

    # use right pointer to expand, left pointer to contract the window

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start_time=time.time()

        if not s or not t:
            return ""
        
        # build a dict of t in s    
        
        dict_t = Counter(t)
        
        required = len(dict_t)
        
        l,r = 0,0
        formed = 0
        window_ct = {}
        ans=(float('inf'), l , r)
        
        while r < len(s):
            
            char=s[r]
            
            window_ct[char]=window_ct.get(char,0) + 1
            
            if char in t and window_ct[char]==dict_t[char]:
                formed+=1
            
            while l<=r and formed == required: # contract the window
                if r-l+1 < ans[0]:
                    ans=(r-l+1,l,r)
                
                window_ct[s[l]]-=1
                char=s[l]
                
                if char in t and window_ct[char]<dict_t[char]:
                    formed-=1
                l+=1
            # expand the right pointer
            r+=1

        end_time=time.time()

        dtime=end_time-start_time
        print("time: ", dtime)


        return "" if ans[0]==float('inf' ) else s[ans[1]:ans[2]+1]

    #-------------------------------------------sliding window
    # better when s in far larger than t and s contains numerous chars that are not in t

    def minWindow2(self, s, t):
        
        if not s or not t:
            return ""
        
        # build a dict of t in s    
        
        dict_t = Counter(t)        
        required = len(dict_t)
        
        # build the filtered_s
        filtered_s=[]
        for i in range(len(s)):
            if s[i] in t:
                filtered_s.append((i,s[i]))
        
        if len(filtered_s)==0: return ""
        
        l,r = filtered_s[0][0],filtered_s[0][0]
        
        formed = 0
        window_ct = {}
        ans=(float('inf'), l , r)
        
        i_r=0
        i_l=0
        while i_r < len(filtered_s):
            
            r = filtered_s[i_r][0]
            char = filtered_s[i_r][1]
            
            window_ct[char]=window_ct.get(char,0) + 1
            
            if window_ct[char]==dict_t[char]:
                formed+=1
            
            while i_l<=i_r and formed == required: # contract the window
                
                l=filtered_s[i_l][0]
                
                if r-l+1 < ans[0]:
                    ans=(r-l+1,l,r)
                                
                char=filtered_s[i_l][1]
                window_ct[char]-=1
                
                if window_ct[char]<dict_t[char]:
                    formed-=1
                i_l+=1
            
            # expand the right pointer
            i_r+=1
        
        return "" if ans[0]==float('inf' ) else s[ans[1]:ans[2]+1]

sol=Solution()
s="AHKJAGSFSDJHFGSA"
t="SADF"
print(sol.minWindow(s,t))
print(sol.minWindow2(s,t))