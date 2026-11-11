class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vis = set()
        for i in  nums:
            if i in vis:
                return True
            else:
                vis.add(i)
        return False