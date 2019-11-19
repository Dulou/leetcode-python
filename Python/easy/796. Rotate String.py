class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if not A:
            return True
        
        flag = A[0]
        store = []
        for i in range(len(B)):
            if B[i] == flag:
                store.append(i)
        
        for i in store:
            if B[i:] + B[:i] == A:
                return True
        return False
        