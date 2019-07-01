class Solution:
    def is_next_bigger(self, s: str) -> int:
        mappings = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        if s not in mappings.keys():
            return 0
        return mappings[s]

    def romanToInt(self, s: str) -> int:
        mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        i = total = 0

        while i < len(s):
            if i + 1 != len(s):
                num = self.is_next_bigger(s[i:i+2])
                if num:
                    total += num
                    i += 1
                else:
                    total += mappings[s[i]]
            else:
                total += mappings[s[i]]
            i += 1

        return total
