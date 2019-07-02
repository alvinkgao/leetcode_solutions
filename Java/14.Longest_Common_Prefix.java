class Solution {
    public String longestCommonPrefix(String[] strs) {
        String res = "";
        if (strs.length == 0)
            return res;
        for (int i = 0; i < strs[0].length(); i++) {
            String letter = strs[0].substring(i, i + 1);
            for (String str : strs) {
                if (i < str.length() && letter.equals(str.substring(i, i + 1)))
                    ;
                else
                    return res;
            }
            res += letter;
        }
        return res;
    }
}