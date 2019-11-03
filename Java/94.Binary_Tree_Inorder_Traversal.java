/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) {
            return new List<Integer>();
        }
        List<Integer> left = inorderTraversal(root.left);
        List<Integer> right = inorderTraversal(root.right);
        List<Integer> res = new List<>();
        res.addAll(left);
        res.add(root.val);
        res.addAll(right);
        return res;
    }
}

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        TreeNode current = root;
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> res = new ArrayList<>();

        while (true) {
            if (current != null) {
                stack.push(current);
                current = current.left;
            } else if (!stack.isEmpty()) {
                current = stack.pop();
                res.add(current.val);
                current = current.right;
            } else {
                break;
            }
        }
        
        return res;
    }
}