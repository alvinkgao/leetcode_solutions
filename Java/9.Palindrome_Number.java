class Solution {
    public boolean isPalindrome(int x) {
        String word = Integer.toString(x);
        if (word.length() <= 1) return true;
        int front = 0;
        int back = word.length() - 1;
        while (front < back) {
            if (word.charAt(front) != word.charAt(back)) return false;
            front++;
            back--;
        } 
        return true;
    }
}