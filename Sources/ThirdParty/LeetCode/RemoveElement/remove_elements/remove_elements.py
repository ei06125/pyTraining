from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        old_size = len(nums)
        print(f"{old_size=}")
        while(nums.count(val)):
            nums.remove(val)
        new_size = len(nums)
        print(f"{new_size=}")
        print(f"{nums=}")
        return new_size