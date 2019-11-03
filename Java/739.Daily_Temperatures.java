class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] res = new int[T.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < T.length; ++i) {
            while (!stack.isEmpty() && T[stack.peek()] < T[i]) {
                int prev_temp_ind = stack.pop();
                res[prev_temp_ind] = i - prev_temp_ind;
            }
            stack.push(i);
        }

        return res;
    }
}