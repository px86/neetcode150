# https://neetcode.io/problems/evaluate-reverse-polish-notation?list=neetcode150

import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(math.trunc(a / b))
                else:
                    pass
            else:
                stack.append(int(token))
        return stack.pop()
