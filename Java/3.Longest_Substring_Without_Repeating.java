import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int total = 0;

        for(int i = 0 , j = 0 ; j < s.length(); ++j) {
            if(map.containsKey(s.charAt(j))) {
                i = Math.max(i, map.get(s.charAt(j)));
            }
            total = Math.max(j - i + 1, total);
            map.put(s.charAt(j), j + 1);
        }
        return total;

    }
}
