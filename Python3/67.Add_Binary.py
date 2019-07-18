class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        m = len(a)
        n = len(b)
        res = ''

        for i in range(max(m,n)):
            a_digit = 0 if i >= m or a[-i-1] == '0' else 1
            b_digit = 0 if i >= n or b[-i-1] == '0' else 1
            total = a_digit + b_digit + carry

            carry = 0 if total < 2 else 1
            res = ('0' if total % 2 == 0 else '1') + res

        return '1' + res if carry else res
