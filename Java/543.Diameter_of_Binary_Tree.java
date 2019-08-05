/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    private int ans = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        depthOfBinaryTree(root);
        return ans;
    }

    private int depthOfBinaryTree(TreeNode root) {
        if (root == null)
            return 0;
        int left = depthOfBinaryTree(root.left);
        int right = depthOfBinaryTree(root.right);
        ans = Math.max(ans, left + right);

        return 1 + Math.max(left, right);
    }
}