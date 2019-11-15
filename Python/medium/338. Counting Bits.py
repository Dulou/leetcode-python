class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        
        res = [0, 1]
        now = 1
        
        for i in range(2, num + 1):
            if i == 2 * now:
                res.append(1)
                now = i
            else:
                res.append(res[now] + res[i - now])
        return res
        