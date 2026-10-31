class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)-1
        mx = arr[n]
        arr[n] =-1
        for i in range(n-1,-1,-1):
            if mx < arr[i]:
                temp = mx
                mx = arr[i]
                arr[i] = temp

            else:
                arr[i]=mx
        return arr            
            
            

        