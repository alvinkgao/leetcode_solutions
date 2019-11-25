class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        cur_mult = 1
        for ind, val in enumerate(nums):
            res[ind] *= cur_mult
            cur_mult *= val

        cur_mult = 1
        for ind, val in enumerate(reversed(nums)):
            res[len(nums) - ind - 1] *= cur_mult
            cur_mult *= val

        return res
