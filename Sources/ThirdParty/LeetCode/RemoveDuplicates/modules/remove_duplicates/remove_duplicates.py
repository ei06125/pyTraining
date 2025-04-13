from typing import List


class Solution:    
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = {}
        for num in nums:
            unique[num] = True
        unique = list(unique)
        k = len(unique)
        for i in range(k):
            nums[i] = unique[i]
        return k
    