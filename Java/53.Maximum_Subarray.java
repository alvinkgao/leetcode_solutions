class Solution {
    public int maxSubArray(int[] nums) {
        int total = nums[0];
        int totalSoFar = total;

        for(int i = 1; i < nums.length; i++) {
            totalSoFar = Math.max(totalSoFar + nums[i], nums[i]);
            total = Math.max(total, totalSoFar);
        }
        return total;
    }
}