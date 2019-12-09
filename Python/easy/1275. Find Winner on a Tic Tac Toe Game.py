class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        record = [0 for i in range(8)]
        
        player = 1
        for move in moves:
            record[move[0]] += player
            record[move[1] + 3] += player
            if move[0] == move[1]:
                record[6] += player
            if move[0] + move[1] == 2:
                record[7] += player
            player *= -1
        
        if 3 in record:
            return 'A'
        if -3 in record:
            return 'B'
        if len(moves) < 9:
            return 'Pending'
        return 'Draw'
        