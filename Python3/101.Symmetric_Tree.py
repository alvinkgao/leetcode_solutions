# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetricHelper(root, root)

    def isSymmetricHelper(self, left: TreeNode, right: TreeNode) -> bool:
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False

        return left.val == right.val and self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)

    def isSymmetricIter(self, root: TreeNode) -> bool:
        queue = deque()
        queue.append(root)
        queue.append(root)
        
        while(queue):
            right = queue.popleft()
            left = queue.popleft()

            if left == None and right == None:
                continue
            if left == None or right == None:
                return False

            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True