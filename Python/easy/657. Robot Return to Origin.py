class Solution:
    def judgeCircle(self, moves: str) -> bool:
        updown = 0
        rightleft = 0
        
        for move in moves:
            if move == 'U':
                updown += 1
            elif move == 'D':
                updown -= 1
            elif move == 'R':
                rightleft += 1
            else:
                rightleft -= 1
        return not updown and not rightleft
        