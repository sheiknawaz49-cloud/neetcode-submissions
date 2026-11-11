class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.presum =[]
        prev_sm = 0
        for i in range(len(nums)):
             prev_sm+= nums[i]
             self.presum.append(prev_sm)
        print(self.presum)

    def sumRange(self, left: int, right: int) -> int:
        if left ==0:
            return self.presum[right]
        else:
            return self.presum[right]-self.presum[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)