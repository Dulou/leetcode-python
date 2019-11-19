class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ')': '(', ']': '[', '}': '{'
        }
        
        stack = []
        for item in s:
            if item in match:
                if not stack or stack.pop() != match[item]:
                    return False
            else:
                stack.append(item)
        return not stack