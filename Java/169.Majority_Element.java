class Solution {
    public int majorityElement(int[] nums) {
        Integer maj = null;
        int count = 0;
        for (int num : nums) {
            if (count == 0) {
                count = 1;
                maj = num;
            }
            else if (num == maj) {
                count += 1;
            }
            else {
                count -= 1;
            }
        }       
        return maj;
    }
}