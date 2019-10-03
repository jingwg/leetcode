class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n=len(A)
        stored_list=[0]*(n+1)
        for i in range(1,n+1):
            num=float('-inf')
            for j in range(1,min(i,K)+1):
                num=max(num,A[i-j])
                stored_list[i]=max(stored_list[i],stored_list[i-j]+num*j)
        return stored_list[n]
        
