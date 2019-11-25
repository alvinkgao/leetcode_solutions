class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        helper(n, 0, new StringBuilder(), ans);
        return ans;
        
    }
    
    private void helper(int open, int close, StringBuilder prefix, List<String> ans) {
        if (open == 0 && close == 0) {
            ans.add(prefix.toString());
            return;
        }

        if (open != 0) {
            helper(open - 1, close + 1, prefix.append('('), ans);
            prefix.deleteCharAt(prefix.length() - 1);
        }
        if (close != 0) {
            helper(open, close - 1, prefix.append(')'), ans);
            prefix.deleteCharAt(prefix.length() - 1);
        }
    }
}