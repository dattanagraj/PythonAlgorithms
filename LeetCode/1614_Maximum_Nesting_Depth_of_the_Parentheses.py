class Solution:
    def maxDepth(self, s: str) -> int:
        nesting_depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                nesting_depth += 1
                if nesting_depth > max_depth:
                    max_depth = nesting_depth
            if c == ')':
                nesting_depth -= 1
        return max_depth
