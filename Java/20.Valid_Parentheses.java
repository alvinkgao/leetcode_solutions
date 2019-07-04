import java.util.HashMap;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put('}', '{');
        mapping.put(']', '[');
        mapping.put(')', '(');

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); ++i) {
            if (mapping.containsKey(s.charAt(i))) {
                char top = !stack.isEmpty() ? stack.pop() : '#'; // # for invalid value
                if (top != mapping.get(s.charAt(i))) {
                    return false;
                }
            } else {
                stack.push(s.charAt(i));
            }
        }
        return stack.isEmpty();

    }
}