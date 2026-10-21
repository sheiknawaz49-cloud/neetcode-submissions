class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) ==1:
            return 1
        if len(arr) ==2:
            if arr[0]==arr[1]:
                return 1
            return 2
        l_ev=0
        l_od = 0
        res_ev,res_od = 1,1
        p=1
        n=1
        for r in range(1,len(arr)):
            if arr[r]==arr[r-1]:
                p=1
                n=1
                l_od=r
                l_ev=r
                continue
            if p == 1 :
                if arr[r-1]<arr[r]:
                    p=-1
                    
                    res_ev = max(res_ev,r-l_ev+1)
                else:
                    l_ev=r-1
            elif p==-1:
                if  arr[r-1]>arr[r]:
                    p=1
                    res_ev = max(res_ev,r-l_ev+1)
                else:
                    l_ev=r-1
            if n == 1 :
                if arr[r-1]>arr[r]:
                    n=-1
                    res_od = max(res_od,r-l_od+1)
                else:
                    l_od=r-1
            elif n==-1:
                if  arr[r-1]<arr[r]:
                    n=1
                    res_od = max(res_od,r-l_od+1)
                else:
                    l_od=r-1
        return max(res_ev,res_od)
            