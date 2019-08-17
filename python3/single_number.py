from collections import defaultdict

def singleNumber(nums):
    record = defaultdict(int)
    for n in nums:
        record[n] += 1

    for key, value in record.items():
        if value == 1:
            return key

print(singleNumber([1,3,3,4,4]))

