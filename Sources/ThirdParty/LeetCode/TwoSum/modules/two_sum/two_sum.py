from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise ValueError("No valid pair found")

class OtherSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i, n in enumerate(nums):
            if n in remainder:
                return [i, remainder[n]]
            remainder[target-n] = i
