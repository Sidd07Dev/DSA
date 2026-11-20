class Solution:
    def findMin(self, nums: list[int]) -> int:
        n= len(nums)
        low,high=0,n-1
        lowest=nums[low]
        while low<=high:
            mid=(int)((low+high)/2)
            if nums[mid]<lowest:
                lowest=nums[mid]
            if nums[mid]<=nums[high]:
                low=mid+1
            else:
                high=mid-1
        low,high=0,n-1
        while low<=high:
            mid=(int)((low+high)/2)
            if nums[mid]<lowest:
                lowest=nums[mid]
            if nums[mid]<=nums[high]:
                
                high=mid-1 
            else:
                low=mid+1
        return lowest