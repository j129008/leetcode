def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    length = len(nums)-1
    i = 0
    while i != length:
        if nums[i] == nums[i+1]:
            nums.pop(i)
            length -= 1
        else:
            i += 1
    return len(nums)

nums = [1, 1, 1, 1, 2]
print('len:', removeDuplicates(nums))
print('ans:', nums)
