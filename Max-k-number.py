# https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/867131730/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i=0
        j=len(nums)-1
        op = 0
        nums.sort()
        while(i<j):
            if nums[i]+nums[j]==k:
                op+=1
                i+=1
                j-=1
            elif nums[i]+nums[j] > k:
                j-=1
            elif nums[i] + nums[j] < k:
                i+=1
        return op