class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int cur_mult = 1;

        for (int i = 0; i < nums.length; ++i) {
            ans[i] = cur_mult;
            cur_mult *= nums[i];
        }

        cur_mult = 1;
        for (int i = nums.length - 1; i >= 0; --i) {
            ans[i] *= cur_mult;
            cur_mult *= nums[i];
        }
        
        return ans;
    }
}