class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table ={}
        for i in range (0,len(nums)):
            left_el = target-nums[i]
            if left_el in hash_table:
                return [i,hash_table[left_el]]
            else:
                hash_table[nums[i]] = i