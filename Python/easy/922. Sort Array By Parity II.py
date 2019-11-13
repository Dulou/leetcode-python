class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        odd_index = []
        even_index = []
        
        for i in range(len(A)):
            if i % 2 == 0 and A[i] % 2 != 0:
                odd.append(A[i])
                if even:
                    A[i] = even.pop()
                else:
                    even_index.append(i)
            if i % 2 != 0 and A[i] % 2 == 0:
                even.append(A[i])
                if odd:
                    A[i] = odd.pop()
                else:
                    odd_index.append(i)
        for i in even_index:
            A[i] = even.pop()
        for i in odd_index:
            A[i] = odd.pop()
        return A
        