class Solution {
    public List<List<Integer>> permute(int[] nums) {

        List<List<Integer>> ans = new ArrayList<>();
        permuteHelper(nums, new ArrayList<>(), ans);
        return ans;

    }

    private void permuteHelper(int[] nums, List<Integer> prefix, List<List<Integer>> ans) {
        if (prefix.size() == nums.length) {
            ans.add(new ArrayList<>(prefix));
            return;
        }

        for (int i = 0; i < nums.length; ++i) {
            if (prefix.contains(nums[i])) {
                continue;
            }
            prefix.add(nums[i]);
            permuteHelper(nums, prefix, ans);
            prefix.remove(prefix.size() - 1);
        }
    }
}