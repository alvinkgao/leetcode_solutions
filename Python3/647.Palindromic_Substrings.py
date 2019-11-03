class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            total += self.extendOut(s, i, i)
            if (i < len(s) - 1):
                total += self.extendOut(s, i, i + 1)
        
        return total
        
    def extendOut(self, s: str, l: int, r: int):
        count = 0
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
            count += 1
        return count
        
