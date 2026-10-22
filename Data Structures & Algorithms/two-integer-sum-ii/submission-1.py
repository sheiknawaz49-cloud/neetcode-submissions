class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        vis = {}
        for i in range(len(numbers)):
            diff = target-numbers[i]
            if diff in vis:
                return [vis[diff]+1,i+1]
            vis[numbers[i]] = i