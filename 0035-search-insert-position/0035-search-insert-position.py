class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low,high=0,len(nums)-1
        mid=(int) ((high+low)/2)
        in_pos=0
        while low<=high:
            mid=(int) ((high+low)/2)
            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                in_pos=mid+1
                low=mid+1
            else:
                high=mid-1

        return in_pos



            