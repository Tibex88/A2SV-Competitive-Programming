// https://leetcode.com/submissions/detail/829211900/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function (nums, target) {
    nums = nums.sort(function (a, b) {
        return a - b
    });
    let newArr = []
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == target) {
            newArr.push(i)
        } else {}
    }
    return newArr

};