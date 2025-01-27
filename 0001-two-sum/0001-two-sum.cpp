class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> valIndexMap;
        for (int i = 0; i < nums.size(); i++){
                valIndexMap[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++){
            if (valIndexMap.find(target - nums[i]) != valIndexMap.end()) {
                int mapIdx = valIndexMap.at(target-nums[i]);
                if (mapIdx != i){
                    return {i, mapIdx};
                }
            }
        } 
    return nums;
    }
};