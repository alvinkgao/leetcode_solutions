import java.util.HashSet;

class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<Character> jewelSet = new HashSet<>();
        int total = 0;
        for (int i = 0; i < J.length(); ++i) {
            jewelSet.add(J.charAt(i));
        }
        for (int j = 0; j < S.length(); ++j) {
            if (jewelSet.contains(S.charAt(j))) {
                ++total;
            }
        }
        return total;
    }
}