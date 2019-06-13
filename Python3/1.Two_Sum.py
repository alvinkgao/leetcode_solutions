class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict();
        for index, num in enumerate(nums):
            if num in seen.keys():
                return [seen[num], index]
            seen[target-num] = index