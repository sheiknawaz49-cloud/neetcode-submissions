class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i]>max_prof:
        #             max_prof = prices[j]-prices[i]
        # return max_prof

        mn=float('inf')
        mx = float('-inf')
        res_set= set()
        for i in prices:
            if i<mn:
                mn=i
                mx = float('-inf')
            elif i>mx:
                mx=i
                max_prof = max(max_prof,mx-mn)
        return max_prof
            
            