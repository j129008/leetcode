class Solution:
    def convertToTitle(self, n: int) -> str:
        # init data
        eng_list = list('ZABCDEFGHIJKLMNOPQRSTUVWXY')
        dig_list = list(range(26))
        eng_map = {dig: eng for eng, dig in zip(eng_list, dig_list)}

        ans = ''
        while n != 0:
            digit = n % 26
            if digit == 0:
                n -= 26
            ans += eng_map[digit]
            n = n // 26

        ans = ans[-1::-1]

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(26))
    print(sol.convertToTitle(701))
    print(sol.convertToTitle(52))
