class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        my_set=set(nums)
        if size == len(my_set):
            return False
        return True

        