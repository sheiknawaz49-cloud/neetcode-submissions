class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sm = 0
        l,r = 0,len(numbers)-1
        while l<r:
            sm = numbers[r]+numbers[l]
            if target == sm:
                return [l+1,r+1]
            elif sm > target:
                r-=1
            else:
                l+=1
