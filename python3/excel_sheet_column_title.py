'''
解題筆記：
26 進位表示數字但是沒有表示 0 的符號, 相反的有代表最大位數的符號
拿 10 進位比喻的話, 就是 0 這個符號不見了, 取而代之的是代表 10 的符號

如果用習慣的方法去計算 (也就是把 0 加回去) 會造成有 A0, B0, C0 等數字, 但這並不合法 (沒有 0), 要用 Z 取代 (Z, AZ, BZ)
但這麼做會讓程式變得不好讀懂, 所以變成了如果遇到 26 整除, 代表 Z 的出現, 並且將總值減去 26 進行計算 (雖然也沒很好懂)

'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        '''
        Z 爲被 26 整除後的代表數字, 但實際上代表進位
        '''
        eng_list = list('ZABCDEFGHIJKLMNOPQRSTUVWXY')
        dig_list = list(range(26))
        eng_map = {dig: eng for eng, dig in zip(eng_list, dig_list)}

        ans = ''
        while n != 0:
            digit = n % 26
            if digit == 0:  # 出現 Z, 減少接下來的進位
                n -= 26
            ans += eng_map[digit]
            n = n // 26

        ans = ans[-1::-1]  # revert string

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(26))
    print(sol.convertToTitle(701))
    print(sol.convertToTitle(52))
