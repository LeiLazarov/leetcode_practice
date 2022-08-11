class Solution:
    def numTrees(self, n: int) -> int:
        ans = [1, 1]
        
        for i in range(2, n+1):
            ans.append(0)
            for j in range(1, i+1):
                ans[i] += ans[j-1] * ans[i-j]
        
        return ans[n]