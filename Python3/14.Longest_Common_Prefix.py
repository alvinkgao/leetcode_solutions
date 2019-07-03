class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        total = ""
        if len(strs) == 0:
            return total
        for i in range(len(strs[0])):
            char = strs[0][i]
            for str in strs:
                if i < len(str) and char == str[i]:
                    pass
                else:
                    return total
            total += char
        return total
