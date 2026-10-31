class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)-1
        l=0
        r=n
        while (l<=r):
            if nums[l] == val and nums[r]!=val:
                temp = nums[l]
                nums[l]= nums[r]
                nums[r] = temp
                l+=1
            elif nums[l] == val and nums[r]==val:
                r-=1
            elif nums[l] != val:
                l+=1
        return l
        