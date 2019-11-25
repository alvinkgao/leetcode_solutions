class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper("", n, 0, ans)
        return ans
        
    def helper(self, prefix, num_starting, num_ending, ans):
        if (num_starting == 0 and num_ending == 0):
            ans.append(prefix)
            return
        
        if (num_starting != 0):
            self.helper(prefix + '(', num_starting - 1, num_ending + 1, ans)
        if (num_ending != 0):
            self.helper(prefix + ')', num_starting, num_ending - 1, ans)