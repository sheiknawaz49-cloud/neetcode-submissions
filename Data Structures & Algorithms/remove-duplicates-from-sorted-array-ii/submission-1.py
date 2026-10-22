class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        ct_l = 1
        while l<r:
            if nums[l]==nums[l+1] and ct_l >1:
                nums[l+1],nums[r]=nums[r],nums[l+1]
                r-=1
                i=l+1
                while i < r:
                    if nums[i]>nums[i+1]:
                        nums[i],nums[i+1]=nums[i+1],nums[i]
                    i+=1
            elif nums[l]==nums[l+1] and ct_l <=1:
                ct_l+=1
                l+=1
            else:
                l+=1
                ct_l=1
        return l+1