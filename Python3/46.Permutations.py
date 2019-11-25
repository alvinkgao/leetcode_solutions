class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.permute_helper(nums, [], ans)
        return ans

    def permute_helper(self, nums, prefix, ans):
        if len(nums) == 0:
            ans.append(prefix.copy())
            return

        for i in range(len(nums)):
            prefix.append(nums[i])
            self.permute_helper(nums[:i] + nums[i + 1:], prefix, ans)
            prefix.pop()
