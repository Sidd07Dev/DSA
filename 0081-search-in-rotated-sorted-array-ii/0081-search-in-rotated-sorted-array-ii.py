class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=(int)((low+high)/2)
            if nums[mid]==target:
                return True
            if nums[low]==nums[high] and nums[high]==nums[mid]:
                low+=1
                high-=1
                continue
            if nums[mid]<=nums[high]:
                if nums[mid]<=target and target <=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target and target <=nums[mid]:
                  high=mid-1
                else:
                    low=mid+1
        

        return False