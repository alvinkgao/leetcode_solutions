class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s.strip()

        length = 0
        n = len(new_str)
        for i in range(n):
            if new_str[n - i - 1] == ' ':
                break
            else:
                length += 1
        return length