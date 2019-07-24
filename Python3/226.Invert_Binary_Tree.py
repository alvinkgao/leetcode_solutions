# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = []
        stack.append(root)

        while (len(stack) != 0):
            node = stack.pop()
            if node == None:
                continue

            temp = node.left
            node.left = node.right
            node.right = temp

            stack.append(node.left)
            stack.append(node.right)
        return root

    def invertTreeRecursive(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        
        right = self.invertTreeRecursive(root.right)
        left = self.invertTreeRecursive(root.left)
        
        root.right = left
        root.left = right

        return root