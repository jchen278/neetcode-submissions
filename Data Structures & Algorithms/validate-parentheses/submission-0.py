class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            print(stack)
            if l == '(' or l == '{' or l == '[':
                stack.append(l)
            elif not stack:
                return False
            elif stack[-1] == '(' and l == ')':
                stack.pop()
            elif stack[-1] == '{' and l == '}':
                stack.pop()
            elif stack[-1] == '[' and l == ']':
                stack.pop()
            else:
                return False
        
        return stack == []