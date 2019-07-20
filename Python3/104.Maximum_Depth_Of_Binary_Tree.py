# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        return self.maxDepthHelper(root, 0)
        
    def maxDepthHelper(self, root: TreeNode, depth: int) -> int:
        if root == None:
            return depth
        
        return 1 + max(self.maxDepthHelper(root.left, depth), self.maxDepthHelper(root.right, depth))

    def maxDepthIter(self, root: TreeNode) -> int:
        if root == None:
            return 0

        stack = []
        h_stack = []
        stack.append(root)
        h_stack.append(0)
        depth = 0

        while(stack):
            cur_node = stack.pop()
            cur_h = h_stack.pop()
            if cur_node == None:
                continue
            depth = max(depth, cur_h + 1)

            stack.append(cur_node.left)
            stack.append(cur_node.right)
            h_stack.append(cur_h + 1)
            h_stack.append(cur_h + 1)

        return depth
        