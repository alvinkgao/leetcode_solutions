class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = list()
        
        for i in range(len(nums)):
            num = abs(nums[i]) - 1
            nums[num] = -abs(nums[num])
                

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res