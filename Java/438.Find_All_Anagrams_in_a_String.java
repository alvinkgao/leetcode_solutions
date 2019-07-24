import java.util.LinkedList;
import java.util.HashMap;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new LinkedList<>();
        if (p.length() > s.length()) return res;
        
        Map<Character, Integer> p_letters = new HashMap<>();
        for (char c : p.toCharArray()) { 
            p_letters.put(c, p_letters.getOrDefault(c, 0) + 1);
        }
        
        int counter = p_letters.size(), begin = 0, end = 0;
        
        while (end < s.length()) {
            char c = s.charAt(end);
            if (p_letters.containsKey(c)) {
                p_letters.put(c, p_letters.get(c) - 1);
                if (p_letters.get(c) == 0) counter--;
            }
            end++;

            while (counter == 0) {
                char tempc = s.charAt(begin);
                if (p_letters.containsKey(tempc)) {
                    p_letters.put(tempc, p_letters.get(tempc) + 1);
                    if (p_letters.get(tempc) > 0) counter++;
                }
                if (end - begin == p.length()) res.add(begin);
                begin++;
            }
        }

        return res;
    }
}