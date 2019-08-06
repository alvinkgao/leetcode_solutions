# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None or t2 == None:
            if t1 == None and t2 == None:
                return None
            return t1 or t2

        cur_node = TreeNode(t1.val + t2.val)
        cur_node.left = self.mergeTrees(t1.left, t2.left)
        cur_node.right = self.mergeTrees(t1.right, t2.right)
        return cur_node
