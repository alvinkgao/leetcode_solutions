class Solution {
    public String addBinary(String a, String b) {
        int carry = 0;
        int m = a.length();
        int n = b.length();
        String res = "";

        int i = m - 1, j = n - 1;
        while(i >= 0 || j >= 0) {
            int a_bit = 0;
            int b_bit = 0;

            if (i >= 0) {
                a_bit = a.charAt(i--) - '0';
            }
            if (j >= 0) {
                b_bit = b.charAt(j--) - '0';
            }
            res = String.valueOf(a_bit ^ b_bit ^ carry) + res;
            carry = (a_bit + b_bit + carry >= 2) ? 1 : 0;
        }
        return carry == 1 ? "1" + res : res;
    
    }
}