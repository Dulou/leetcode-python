class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        length = len(values)
        l = [[labels[i], values[i]] for i in range(length)]
        
        l.sort(key=lambda x:x[1], reverse=True)
        
        res = 0
        num = 0
        store = {}
        
        for item in l:
            store[item[0]] = store.get(item[0], 0) + 1
            if store[item[0]] <= use_limit:
                num += 1
                res += item[1]
            if num == num_wanted:
                break
        return res
            
        