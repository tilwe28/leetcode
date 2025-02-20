class NumArray {
public:
    NumArray(vector<int>& nums) {
        prefix.resize(nums.size());
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            prefix[i] = sum;
        }
    }
    
    int sumRange(int left, int right) {
        return prefix[right] - (left > 0 ? prefix[left - 1] : 0);
    }

    vector<int> prefix;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */