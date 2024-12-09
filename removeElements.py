from typing import List


class RemoveElements:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        k = 0
        
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k