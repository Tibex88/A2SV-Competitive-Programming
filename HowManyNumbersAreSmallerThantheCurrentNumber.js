// https://leetcode.com/submissions/detail/829205365/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
    let resArr = new Array(nums.length).fill(0);
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (nums[i] != nums[j] && nums[i] > nums[j]) {
                resArr[i] += 1
            }
        }
    }
    return resArr
};