"""
refer the leetcode solution
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == "" or t == "":
            return ""
        
        dict = {}
        unique_t = 0
        for char in t:
            if char not in dict:
                dict[char] = 0
                unique_t += 1
            dict[char] += 1
        
        start, end = 0, 0
        length = len(s)
        res_len = length + 1
        left, right = 0, 0
        
        while end < length:
            if s[end] in dict:
                dict[s[end]] -= 1
                if dict[s[end]] == 0:
                    unique_t -= 1
            while start <= end and unique_t == 0:
                if end - start + 1 < res_len:
                    res_len = end -start + 1
                    left, right = start, end
                if s[start] in dict:
                    dict[s[start]] += 1
                    if dict[s[start]] > 0:
                        unique_t += 1
                start += 1
            end += 1
        
        return "" if res_len == length + 1 else s[left:right+1]
        
        
        
        
        