class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '}' : '{',
            ']' : '[',
            ')' : '('
            }
        stack = list()

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#' #dummy value
                if top != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack