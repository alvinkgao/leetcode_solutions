class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T)):
            # while there are temperatures to fill and temperatures are lower
            while (stack and T[stack[-1]] < T[i]):
                prev_temp_ind = stack.pop()
                res[prev_temp_ind] = i - prev_temp_ind
            stack.append(i)

        return res
