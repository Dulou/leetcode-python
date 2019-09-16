class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(A, B):
            return A if B == 0 else gcd(B, A%B)
        lcm = A * B / gcd(A, B)
        layout = lcm // A + lcm // B - 1
        layout_num = N // layout
        layout_left_num = N % layout

        left = 0
        right = lcm
        while left < right:
            mid = (left + right) // 2
            if (mid // A + mid // B) < layout_left_num:
                left = mid + 1
            else:
                right = mid
        return int((lcm * layout_num + right) % (10**9 + 7))
