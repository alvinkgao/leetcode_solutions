class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels_set = set()
        total = 0;
        for char in J:
            jewels_set.add(char)
        for stone in S:
            if stone in jewels_set:
                total += 1
        return total
