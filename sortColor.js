// https://leetcode.com/problems/sort-colors/submissions/
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    for(let i=0; i<nums.length; i++){
        for(let j=0; j<nums.length-1;j++){
            if(nums[j]>nums[j+1]){
                let temp = ""
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
        }
        }
    }
    return nums
};
