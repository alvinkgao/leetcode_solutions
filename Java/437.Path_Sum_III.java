/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.HashMap;

class Solution {
    public int pathSum(TreeNode root, int sum) {
        if (root == null) return 0;
        Map<Integer,Integer> prefixSum = new HashMap<>();
        prefixSum.put(0,1);

        return pathSumHelper(root, 0, sum, prefixSum);
    }

    public int pathSumHelper(TreeNode root, int sum, int target, Map<Integer,Integer> prefixSum) {
        if (root == null) return 0;
        sum += root.val;

        int numPathsToCur = 0;
        if (prefixSum.containsKey(sum - target)) numPathsToCur = prefixSum.get(sum - target);

        if (prefixSum.containsKey(sum)) {
            prefixSum.put(sum, prefixSum.get(sum) + 1);
        } else {
            prefixSum.put(sum, 1);
        }

        int res = numPathsToCur + pathSumHelper(root.left, sum, target, prefixSum) + pathSumHelper(root.right, sum, target, prefixSum);
        prefixSum.put(sum, prefixSum.get(sum) - 1);

        return res;

    }
}