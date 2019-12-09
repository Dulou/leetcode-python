class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        store = {}
        length = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in store:
                store[groupSizes[i]].append(i)
            else:
                store[groupSizes[i]] = [i]
            
            length[groupSizes[i]] = length.get(groupSizes[i], 0) + 1
            if length[groupSizes[i]] == groupSizes[i]:
                res.append(store[groupSizes[i]])
                store[groupSizes[i]] = []
                length[groupSizes[i]] = 0
        return res