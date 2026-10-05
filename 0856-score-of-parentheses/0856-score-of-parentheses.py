class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                inner_score = stack.pop()
                current_score = max(2*inner_score, 1)
                stack[-1]+= current_score
        return stack[0]
