class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)) :
                    if nums[i] + nums[j] == target:
                        return [i,j]

    def twoSumm(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,num in enumerate(nums):
            if target - num in dict :
                return [dict[(target-num),i]]
            else:
                dict[num] = i