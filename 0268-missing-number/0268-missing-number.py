class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum = 0 
        for i in nums:
            sum+=i
        
        exp_total = int( (n*(n+1))/2)
        diff = sum - exp_total
        if diff>0:
            return diff
        else:
          return diff * (-1)