class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        length = len(stones)
        if length == 1:
            return stones[0]
        
        while length >= 2:
            stones.sort(reverse=True)
            if stones[0] == stones[1]:
                stones[0], stones[1] = 0, 0
                length -= 2
            else:
                stones[0] = abs(stones[0] - stones[1])
                stones[1] = 0
                length -= 1
        
        if length == 0:
            return 0
        else:
            stones.sort(reverse=True)
            return stones[0]
        