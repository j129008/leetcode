class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [False, True] + [True] * (n-2)
        count = 0
        for i in range(2, n):
            if prime[i] is False:
                continue
            count += 1
            for j in range(i*i, n, i):
                prime[j] = False
        return count


if __name__ == '__main__':
    print(Solution().countPrimes(10))
