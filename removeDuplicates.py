def removeDuplicates(nums: list) -> int:
    temp = 0
    for i in range(0, len(nums)):
        if nums[i] != nums[temp]:
            temp += 1
            nums[temp] = nums[i]

    return temp + 1


print(removeDuplicates([1, 1, 2, 3]))
