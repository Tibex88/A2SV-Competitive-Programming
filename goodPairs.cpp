// https://leetcode.com/problems/number-of-good-pairs/submissions/867081080/

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count=0;
        for(int i=0 ; i<nums.size()-1; i++){
            for(int j=i+1; j<nums.size(); j++){
            if(nums[i]==nums[j])
                count++;
        }
        }
        return count;
    }
};