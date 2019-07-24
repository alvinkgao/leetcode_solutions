# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.pathSumHelper(root, sum, [])
        
    def pathSumHelper(self, root: TreeNode, sum: int, parentList: List[int]) -> int:
        cur_list = list(parentList)
        if root == None:
            return 0
        counter = 0
        for i in range(len(cur_list)):
            cur_list[i] += root.val
            if cur_list[i] == sum:
                counter += 1
        if sum == root.val:
            counter += 1
        cur_list.append(root.val)
        return counter + self.pathSumHelper(root.left, sum, cur_list) + self.pathSumHelper(root.right, sum, cur_list)
        
             
            

#optimal solution
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0;
        prefix_sums = {0: 1}
        return self.pathSumHelper(root, 0, sum, prefix_sums)

    def pathSumHelper(self, root: TreeNode, sum: int, target: int, prefix_sums: dict) -> int:
        if root == None:
            return 0;
        sum += root.val

        num_path_to_cur = 0
        if (sum - target) in prefix_sums.keys():
            num_path_to_cur = prefix_sums[sum - target]

        if sum in prefix_sums.keys():
            prefix_sums[sum] += 1
        else:
            prefix_sums[sum] = 1
        
        res = num_path_to_cur + pathSumHelper(root.left, sum, target, prefix_sums) + pathSumHelper(root.right, sum, target, prefix_sums)
        prefix_sums[sum] -= 1

        return res


