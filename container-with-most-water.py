#  https://leetcode.com/problems/container-with-most-water/submissions/878662008/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r =0, len(height)-1

        while l<r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)

            if height[l]< height[r]:#except this 
                l+=1
            else: 
                r-=1
        return res