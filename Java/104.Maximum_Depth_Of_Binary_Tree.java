/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.Stack;

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return maxDepthHelper(root, 0);
    }
    
    public int maxDepthHelper(TreeNode root, int cur_depth) {
        if (root == null) return cur_depth;
        return 1 + Math.max(maxDepthHelper(root.left, cur_depth), maxDepthHelper(root.right, cur_depth));
        
    }

    public int maxDepthIter(TreeNode root) {
        if (root == null) return 0;
        Stack<TreeNode> stack = new Stack<>();
        Stack<Integer> depth_stack = new Stack<>();
        int depth = 0;

        TreeNode stack.push(root);
        int depth_stack.push(0);

        while (!stack.isEmpty()) {
            cur_node = stack.pop();
            cur_depth = depth_stack.pop();

            if (cur_node == null) continue;

            depth = Math.max(depth, cur_depth + 1);

            depth_stack.push(cur_depth + 1);
            depth_stack.push(cur_depth + 1);
            stack.push(cur_node.left);
            stack.push(cur_node.right);
        }

        return depth;

    }
}