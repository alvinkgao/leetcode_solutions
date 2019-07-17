class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits
        else:
            number = 0
            for i in digits:
                number *= 10
                number += i
            number += 1
            number = str(number)
            res = []
            for i in number:
                res.append(i)
            return res
