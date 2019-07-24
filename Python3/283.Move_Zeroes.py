class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_counter = 0
        i = 0
        
        while i + zero_counter < n:
            if nums[i + zero_counter] == 0:
                zero_counter += 1
            else:
                if zero_counter > 0:
                    nums[i] = nums[i + zero_counter]
                i += 1
        
        while i < n:
            nums[i] = 0
            i += 1

