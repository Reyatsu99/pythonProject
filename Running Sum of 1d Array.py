def runningSum(nums: list[int]) -> list[int]:
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i] = nums[i] + temp
        temp = nums[i]
    return nums


print(runningSum([1, 1, 1, 1]))
