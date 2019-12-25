class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), ans);
        return ans;
    }

    private void backtrack(int[] candidates, int target, int index, List<Integer> prefix, List<List<Integer>> ans) {
        if (target < 0) {
            return;
        } else if (target == 0) {
            ans.add(new ArrayList<>(prefix));
        } else {
            for (int i = index; i < candidates.length; ++i) {
                prefix.add(candidates[i]);
                backtrack(candidates, target - candidates[i], i, prefix, ans);
                prefix.remove(prefix.size() - 1);
            }
        }
    }
}