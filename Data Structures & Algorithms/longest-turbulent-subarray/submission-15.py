class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if not arr:
            return 0
        
        # 'inc' tracks the max length ending with arr[i] > arr[i-1]
        # 'dec' tracks the max length ending with arr[i] < arr[i-1]
        inc, dec = 1, 1
        max_len = 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                # If we go up, the previous step MUST have gone down
                inc = dec + 1
                dec = 1 # Reset the 'down' tracker
            elif arr[i] < arr[i-1]:
                # If we go down, the previous step MUST have gone up
                dec = inc + 1
                inc = 1 # Reset the 'up' tracker
            else:
                # If they are equal, both patterns break
                inc = 1
                dec = 1
                
            max_len = max(max_len, inc, dec)
            
        return max_len