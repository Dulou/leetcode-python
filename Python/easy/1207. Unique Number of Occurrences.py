class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            count[i] = count.get(i, 0) + 1
        
        occur = {}
        for k in count:
            if count[k] in occur:
                return False
            else:
                occur[count[k]] = 0
        return True
        