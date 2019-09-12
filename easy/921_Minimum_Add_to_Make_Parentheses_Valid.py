class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if stack == []:
                stack.append(s)
                continue
            if s == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
        return len(stack)