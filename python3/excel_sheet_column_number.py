'''
excel_sheet_column_title 的反算, 只要根據每個位數的加權去計算即可
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        eng_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        dig_list = list(range(1, 27))
        dig_map = {eng: dig for eng, dig in zip(eng_list, dig_list)}
        revert_s = s[-1::-1]

        weight = 1
        value = 0
        for rs in revert_s:
            value += weight * dig_map[rs]
            weight *= 26

        return value


if __name__ == '__main__':
    sol = Solution()
    print(sol.titleToNumber('ZY'))
