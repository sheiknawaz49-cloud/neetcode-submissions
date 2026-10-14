class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        
        # 2. Create buckets where the index is the frequency. 
        # Size is len(nums) + 1 because a number can appear at most len(nums) times.
        freq = [[] for _ in range(len(nums) + 1)]
        
        # 3. Populate buckets: freq[frequency] = [list of numbers]
        for num, c in count.items():
            freq[c].append(num)
            
        # 4. Gather the top k elements by iterating backwards (highest frequency first)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res