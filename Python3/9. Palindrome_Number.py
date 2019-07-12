class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        if len(word) <= 1:
            return True
        front = 0
        back = len(word) - 1
        while word[front] < word[back]:
            if word[front] != word[back]:
                return False
            front += 1
            back -= 1
        return True
