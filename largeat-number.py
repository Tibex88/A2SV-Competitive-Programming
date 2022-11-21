# https://leetcode.com/submissions/detail/847326117/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if not any(map(bool, nums)):
            return '0'
        
        nums = list(map(str, nums))
        
        if len(nums) < 2:
            return "".join(nums)
        
        def compare(x,y):
            return int(nums[x]+ nums[y]) > int(nums[y]+ nums[x]);
    
        for x in range(len(nums) -1):
            y = x+1
            while x< len(nums) and y <len(nums):
                if compare(x,y):
                    pass
                else:
                    nums[x], nums[y] = nums[y], nums[x];
                y+=1;

        return "".join(nums) ; 