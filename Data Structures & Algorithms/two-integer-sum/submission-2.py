class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, x in enumerate(nums):
            difference = target - x
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[x] = i
         



