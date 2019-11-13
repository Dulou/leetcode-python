class Solution:
    def selfDividing(self, num):
        tmp = num
        while tmp > 0:
            div = tmp % 10
            if div == 0 or num % div != 0:
                return False
            tmp = tmp // 10
        return True
            
        
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            if self.selfDividing(num):
                res.append(num)
        return res
            
            
                
        