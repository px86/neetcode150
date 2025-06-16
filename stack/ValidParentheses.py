# https://neetcode.io/problems/validate-parentheses?list=neetcode150


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if x == "(" and char != ")":
                    return False
                if x == "{" and char != "}":
                    return False
                if x == "[" and char != "]":
                    return False
        return len(stack) == 0
