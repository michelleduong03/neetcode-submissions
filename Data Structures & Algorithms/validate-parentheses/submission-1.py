class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''

        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs:  # If it's a closing bracket
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)  # Push opening bracket

        return not stack  # Valid if stack is empty