from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n_dict = dict()
        for n in range(len(numbers)):
            n_dict[numbers[n]] = n

        n_num = sorted(n_dict.keys())
        num_len = len(n_num)
        for i in range(num_len):
            for j in range(i+1, num_len):
                if n_num[i] + n_num[j] == target:
                    return [n_dict[n_num[i]]+1, n_dict[n_num[j]]+1]

        for num in n_num:
            if num + num == target:
                return [n_dict[num], n_dict[num]+1]


if __name__ == '__main__':
    print(Solution().twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8))
