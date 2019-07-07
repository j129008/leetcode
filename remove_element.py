def removeElement(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j


nums = [3, 2, 2, 3]
length = removeElement(nums, 3)
print('ans:', nums[:length])
