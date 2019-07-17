class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0] 
        total_so_far = total

        for i in range(len(nums) - 1):
            total_so_far = max(total_so_far + nums[i + 1], nums[i + 1])
            total = max(total, total_so_far)
        return total