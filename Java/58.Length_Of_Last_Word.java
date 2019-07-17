class Solution {
    public int lengthOfLastWord(String s) {
        String new_str = s.trim();

        int length = 0;
        for (int i = new_str.length() - 1; i >= 0; --i) {
            if (new_str.charAt(i) == ' ') break;
            else length += 1;
        }   
        return length;
    }
}}