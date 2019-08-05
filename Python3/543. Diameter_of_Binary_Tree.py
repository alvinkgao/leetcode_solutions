# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.depthOfTree(root)
        return self.ans

    def depthOfTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.depthOfTree(root.left)
        right = self.depthOfTree(root.right)
        ans = max(ans, left + right)
        return 1 + max(left, right)



