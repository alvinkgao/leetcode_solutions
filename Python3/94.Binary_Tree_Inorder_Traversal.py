# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if (root == None):
            return []
        left = self.inorderTraversal(self, root.left)
        right = self.inorderTraversal(self, root.right)
        res = left + [root.val] + right
        return res


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root
        res = []
        stack = []

        while (True):
            if current != None:
                stack.append(current)
                current = current.left
            elif (stack):
                current = stack.pop()
                res.append(current.val)
                current = current.right
            else:
                break

        return res
