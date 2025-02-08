class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0){
            return -1;
        } 
        if (nums.size() == 1){
            return (nums[0] == target) -1;
        }
        int mid = nums.size()/2;
        if(nums[mid] == target){
            return mid;
        }
        if (nums[mid] < target){
            vector<int> newV = vector<int>(nums.begin() + mid, nums.begin() + nums.size());
            int right_search = search(newV, target); 
            return right_search < 0? right_search: mid + right_search; 
        }
        if (nums[mid] > target){
            vector<int> newV = vector<int>(nums.begin(), nums.begin()+mid);
            return search(newV, target);
            }
        return -2; //Shouldn't happen
        }
};