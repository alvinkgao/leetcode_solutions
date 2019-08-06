# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.total = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root != None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

#recursive but no global variable
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.convertBSTHelper(root, 0)
        return root
    
    def convertBSTHelper(self, root: TreeNode, total: int) -> int:
        if root == None: 
            return total 

        right = self.convertBSTHelper(root.right, total)        
        root.val += right
        left = self.convertBSTHelper(root.left, root.val)
        return left

#unfinished iterative
class Solution:
    def convertBST(self, root: TreeNode):
        if root == None:
            return root
        
        stack = []
        stack.append(root)
        total = 0

        while len(stack) != 0:
            node = stack.pop()
            if node == None:
                continue
            
            stack.append(node.right)

            node.val += total
            total = node.val
            stack.append(node.left)
            

        return root