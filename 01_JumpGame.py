# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 12:20:51 2021

@author: Tian

Jump Game

https://leetcode.com/problems/jump-game/solution/

"""


class Solution(object):

    #-------------------------check each zero, canJump returns true only when all 0s can be stepped over
    # O(n)
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1: return True
        
        zero_idx=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                zero_idx.append(i)
        
        if len(zero_idx) == 0 : #no zero found in the list
            return True
        else:
            for idx in zero_idx: # check each 0
                cross = self.checkstep(idx, nums)
                if not cross:
                    return False
            return True


    def checkstep(self, idx, nums):
        if idx==len(nums)-1:
            for i in range(idx-1,-1,-1):
                if i +nums[i] >= idx:
                    return True
            return False
        else:
            for i in range(idx-1,-1,-1):
                if i +nums[i] > idx:
                    return True
            return False

    #-------------------------step1: recursive backtracking, O(n^2)
    def canJump1(self, nums):
        return self.canJumpfromPosition(0, nums)

    def canJumpfromPosition(self, position, nums):
        if position == len(nums)-1:
            return True

        reachable_position = min (position + nums[position], len(nums)-1)
        for i in range(position+1, reachable_position+1):
            if self.canJumpfromPosition(i, nums):
                return True
        return False


    #-------------------------step2: memoziation, dynamic programming (top-down), O(n^2)
    memo=[]

    def canJump2(self, nums):

        self.memo=['U' for i in range(len(nums))]
        self.memo[-1]='G'

        print(self.memo)

        return self.canJumpfromPosition2(0, nums)


    def canJumpfromPosition2(self, position, nums):
        if self.memo[position]=='G':
            return True

        reachable_position = min (position + nums[position], len(nums)-1)
        for i in range(position+1, reachable_position+1):
            if self.canJumpfromPosition2(i, nums):
                self.memo[i]='G'
                self.memo[position]='G'
                return True
        return False

    #-------------------------step3: Dynamic Programming Bottom-up, eliminating the recursion
    # (eliminate the stack overhead), open for futher optimization, O(n^2)
    def canJump3(self, nums):

        self.memo=['U' for i in range(len(nums))]
        self.memo[-1]='G'

        for i in range(len(nums)-2,-1,-1):
            reachable_position = min (i + nums[i], len(nums)-1)
            for j in range(i+1, reachable_position+1):
                if self.memo[j] == 'G':
                    self.memo[i]='G'
                    break

        return self.memo[0]=='G'

    #-------------------------step4: optimize by tricks, greedy, only keep trakc of the first good index
    #O(n)
    def canJump4(self, nums):
        last_position=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i]>=last_position:
                last_position=i

        return last_position == 0



sol=Solution()
nums=[3,2,1,0,4]
print(sol.canJump(nums))

print(sol.canJump1(nums))

print(sol.canJump2(nums))

print(sol.canJump3(nums))

print(sol.canJump4(nums))