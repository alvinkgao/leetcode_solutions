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
    int total = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root != null) {
            convertBST(root.right);
            total += root.val;
            root.val = total;
            convertBST(root.left);
        }
        
        return root;
    }
}

class Solution {
    public TreeNode convertBST(TreeNode root) {
        if (root == null) return root;
        convertBSTHelper(root, 0);
        return root;
    }
    
    private int convertBSTHelper(TreeNode root, int total) {
        if (root == null) return total;

        int right = convertBSTHelper(root.right, total);
        root.val += right;
        int left = convertBSTHelper(root.left, root.val);
        
        return left;
    }
}

