class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sm = []
        sm = 0
        for i in nums:
            sm +=i
            pre_sm.append(sm)
        for i in range(len(nums)):
            right = pre_sm[i-1] if i>1 else 0
            if pre_sm[i] == pre_sm[len(nums)-1]-right:
                return i
        return -1