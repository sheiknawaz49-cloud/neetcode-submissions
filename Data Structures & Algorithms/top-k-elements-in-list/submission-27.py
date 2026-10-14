class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vis = {}
        freq = [0]
        freq_vis = {}
        for i in nums:
            vis[i] = vis.get(i,0)+1
            if vis[i]>=freq[-1]:
                freq.append(vis[i])
            freq_vis[vis[i]] = freq_vis.get(vis[i],set())
            freq_vis[vis[i]].add(i)
        res = set()
        for i in freq[::-1]:
            res= res | freq_vis[i]
            if len(res) >=k:
                return list(res)

        