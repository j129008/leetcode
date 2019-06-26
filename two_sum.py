def twoSum(nums, target):
    need_dict = dict()
    for i in range(len(nums)):
        need = target - nums[i]
        if need in need_dict:
            return [i, need_dict[need]]
        need_dict[nums[i]] = i

print(twoSum([3,3], 6))
