def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] >= target:
            return i
    return i+1

print(searchInsert([1, 3, 5, 6], 7))
