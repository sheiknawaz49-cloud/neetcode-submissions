class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        sm = sum(arr[0:k])
        if sm >= threshold*k:
            res =1
        for i in range(1,len(arr)-k+1):
            sm = sm - arr[i-1]+arr[i+k-1]
            if sm>= threshold*k:
                res +=1
        return res