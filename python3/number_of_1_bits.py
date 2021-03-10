class Solution:
    def hammingWeight(self, n: int) -> int:
        sign_bit_count = 1 if n < 0 else 0
        abs_n = abs(n)

        bit_count = 0
        while abs_n != 0:
            bit_count += abs_n % 2
            abs_n = abs_n // 2

        return bit_count + sign_bit_count

