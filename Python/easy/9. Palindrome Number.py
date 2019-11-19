class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        l = len(s) // 2
        r = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
        return True if len(s) == 1 else s[:l] == s[r:][::-1]
        
        
        