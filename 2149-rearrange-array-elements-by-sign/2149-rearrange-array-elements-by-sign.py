class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
      l = len(nums)
      result = [0]*l
      pos,neg=0,1
      for i in range (0,l):
        if nums[i]>0:
            result[pos]=nums[i]
            pos=pos+2
        else:
            result[neg]=nums[i]
            neg=neg+2

      return result

        