class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up, left = 0, 0
        for move in moves:
            if move == 'U': up += 1
            elif move == 'D': up -= 1
            elif move == 'L': left += 1
            else: left -= 1
        return up==0 and left==0

    """
    one sentence code:
    return return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
    """