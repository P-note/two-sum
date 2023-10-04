from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return

# t = twoSum(nums = [3,3], target= 6)
# print(t)