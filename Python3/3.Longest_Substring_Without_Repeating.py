class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        total = 1
        i = j = 0
        contains = dict()
        for j in range(len(s)):
            if s[j] in contains.keys():
                i = max(contains[s[j]], i)
            total = max(j - i + 1, total)
            contains[s[j]] = j + 1
        return total

        '''
        contains.add(s[0])

        while j < len(s) - 1:
            j += 1
            if s[j] not in contains:
                contains.add(s[j])
                total = max(j - i + 1, total)
            else:
                while 1:
                    if i == j:
                        break
                    elif s[i] == s[j]:
                        i += 1
                        break
                    else:
                        contains.remove(s[i])
                        i += 1
        '''
        return total
