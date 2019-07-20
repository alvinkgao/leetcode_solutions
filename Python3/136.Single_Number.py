class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            nums[0] ^= nums[i+1]
        return nums[0]