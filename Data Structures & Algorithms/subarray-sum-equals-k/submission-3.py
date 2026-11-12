class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sm = []
        sm = 0
        pre_sm_st = set()
        for i in nums:
            sm+=i
            pre_sm.append(sm)
            pre_sm_st.add(sm)
        print(pre_sm,pre_sm_st)
        res = 0
        for i in range(len(pre_sm)):
            if pre_sm[i]==k:
                res+=1
            if k+pre_sm[i] in pre_sm_st:
                for j in range(i+1,len(pre_sm)):
                    if pre_sm[j]-pre_sm[i]==k:
                        print(j,i, pre_sm[j],pre_sm[i])
                        res+=1
        return res
