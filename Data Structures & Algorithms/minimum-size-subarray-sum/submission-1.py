class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_sz = float("inf")
        l=0
        sm = 0
        found = False
        for r in range(len(nums)):
            sm+=nums[r]
            while sm>=target:
                found = True
                min_sz = min(min_sz, r-l+1)
                sm-=nums[l]
                l+=1
        if not found:
            return 0
        return min_sz

        