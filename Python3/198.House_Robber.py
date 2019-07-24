class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev1 = 0
        prev2 = 0

        for num in nums:
            temp = prev1
            prev1 = max(prev1, num + prev2)
            prev2 = temp
        return prev1

#with memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            dp[i+2] = max(dp[i+1], nums[i] + dp[i])
            print(dp)
        print(dp)
        return dp[len(nums) + 1]