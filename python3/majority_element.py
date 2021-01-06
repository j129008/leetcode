'''
解題筆記：
計算陣列值出現次數, 如果過半就是主要組成數字
題目限制複雜度 O(n), 用 dict 掃過一遍記錄即可
如果用 defaultdict 程式會更漂亮 (不需要 try/except)
'''

class Solution:
    def majorityElement(self, nums) -> int:
        counter = {}
        for ele in nums:
            try:
                counter[ele] += 1
            except:
                counter[ele] = 1

        nums_len = len(nums)
        for key, value in counter.items():
            if value > nums_len // 2:
                return key
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([1]))
    print(sol.majorityElement([2, 2, 1, 2, 2]))
