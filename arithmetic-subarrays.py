# https://leetcode.com/problems/arithmetic-subarrays/submissions/878543240/
class Solution:
    
    def checker(self,nums):
        i = 2
        n = len(nums)
        diff = nums[1] - nums[0]
        while i < n:
            if nums[i] - nums[i-1] != diff:
                return False
            i += 1
        return True
    
    def checkArithmeticSubarrays(self, nums: List[int], left: List[int], right: List[int]) -> List[bool]:
        m, i, ans = len(left), 0, []
        while i < m:
            l, r = left[i], right[i]
            sub = nums[l:r+1]
            sub.sort()
            ans.append(self.checker(sub))
            i += 1
        return ans