class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #模仿栈结构
        stack = []
        i = -1
        for char in s:
            if char==')':
                if i==-1:
                    return False
                elif stack[i]=='(':
                    del stack[i]
                    i -= 1
                else:
                    stack.append(char)
                    i += 1
            elif char == '}':
                if i==-1:
                    return False
                elif stack[i]=='{':
                    del stack[i]
                    i -= 1
                else:
                    stack.append(char)
                    i += 1
            elif char == ']':
                if i==-1:
                    return False
                elif stack[i]=='[':
                    del stack[i]
                    i -= 1
                else:
                    stack.append(char)
                    i += 1
            else:
                stack.append(char)
                i += 1
        return True if stack==[] else False

if __name__ == "__main__":
    f = raw_input()
    a = Solution()
    while f:
        print a.isValid(f)
        f = raw_input()
