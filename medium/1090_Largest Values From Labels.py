from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        store = [(value, label) for value, label in zip(values, labels)]
        store.sort(key=lambda a: a[0], reverse=True)

        store_num = {}
        res = 0
        i = 0
        for _ in range(num_wanted):
            while i < len(store) and store_num.get(store[i][1], 0) >= use_limit:
                i += 1
            if i == len(store):
                break
            store_num[store[i][1]] = store_num.get(store[i][1], 0) + 1
            res += store[i][0]
            i += 1
        return res

if __name__ == "__main__":
    print(Solution().largestValsFromLabels([5,4,3,2,1],[1,3,3,3,2],3,2))

