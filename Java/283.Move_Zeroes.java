class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int i = 0, zero_count = 0;
        while (i + zero_count < n) {
            if (nums[i + zero_count] == 0) ++zero_count;
            else {
                nums[i] = nums[i + zero_count];
                ++i;
            }
        }
        while (i < n) {
            nums[i++] = 0;
        }
    }
}