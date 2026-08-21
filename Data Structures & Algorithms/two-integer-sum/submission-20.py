class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       myMap = {}

       for idx, val in enumerate(nums):
            diff = target - val
            if diff in myMap:
                return [myMap[diff], idx]
            myMap[val] = idx
