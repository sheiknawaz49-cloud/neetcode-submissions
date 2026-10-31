class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        consecutive=0
        for i in nums:
            if i == 1:
                consecutive+=1
            else:
                max_consecutive = max_consecutive if max_consecutive>=consecutive else consecutive
                consecutive = 0
            max_consecutive = max_consecutive if max_consecutive>=consecutive else consecutive

            
        return max_consecutive
        