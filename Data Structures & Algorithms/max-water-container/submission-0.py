class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r,max_res = 0,len(heights)-1,float('-inf')
        while r>l:
            res = min(heights[l],heights[r])*(r-l)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
            max_res = max(res, max_res)
        return max_res