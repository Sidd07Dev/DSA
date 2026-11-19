class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low,high=0,len(nums)-1
        start,end=-1,-1
        while low<=high:
            mid=(int)((low+high)/2)
            if nums[mid] == target:
                    end = mid
            if nums[mid]<= target:
                low=mid+1
            else:
                high=mid-1
        low,high=0,len(nums)-1
        while low<=high:
            mid=(int)((low+high)/2)
            if nums[mid] == target:
                    start = mid
            if nums[mid]>= target:
                high=mid-1
            else:
                low=mid+1
        return [start,end]
