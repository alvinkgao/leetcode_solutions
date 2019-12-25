class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sorted_candidates = sorted(candidates) #not required 
        self.backtrack(sorted_candidates, target, 0, list(), ans)
        return ans
    
    def backtrack(self, candidates, target, index, prefix, ans):
        if target < 0:
            return
        if target == 0:
            ans.append(prefix.copy())
            return
        for i in range(index, len(candidates)):
            prefix.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i, prefix, ans)
            prefix.pop()