# https://neetcode.io/problems/generate-parentheses?list=neetcode150

from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        permutations = []

        def func(s: str, lparen_count: int, rparen_count: int):

            if len(s) == 2 * n:
                if lparen_count == rparen_count:
                    permutations.append(s)
                return

            # non balanced at this point, so skip this path
            if rparen_count > lparen_count:
                return

            func(s + "(", lparen_count + 1, rparen_count)
            func(s + ")", lparen_count, rparen_count + 1)

        func("", 0, 0)
        return permutations
