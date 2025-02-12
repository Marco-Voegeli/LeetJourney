#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> valIndexMap;
        for (int i = 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if (valIndexMap.find(complement) != valIndexMap.end()){
                return {valIndexMap[complement], i};
            }
            valIndexMap[nums[i]] = i;

        }
        return {};
    }
};