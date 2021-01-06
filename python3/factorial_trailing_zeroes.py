'''
計算 n! 的數字後面有幾個 0, 所以算因數的 2 跟 5 有幾個, 取最小的即可
可以用填表加速計算, 但懶得寫, 我就爛
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        two = 0
        five = 0
        for i in range(1, n+1):
            while i % 2 == 0:
                i = i // 2
                two += 1

            while i % 5 == 0:
                i = i // 5
                five += 1

        return min(two, five)


if __name__ == '__main__':
    sol = Solution()
    print(sol.trailingZeroes(3))
    print(sol.trailingZeroes(5))
    print(sol.trailingZeroes(0))
