import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<Integer,Integer>();
        for (int i = 0; i < nums.length; ++i) {
            if (seen.containsKey(nums[i])) {
                return new int[]{seen.get(nums[i]), i};
            }
            seen.put(target-nums[i], i);
        }        
        throw new IllegalArgumentException("No solution");
    }
}