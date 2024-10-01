class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        
        no_del = [0] * n
        one_del = [0] * n
        
        no_del[0] = arr[0]
        one_del[0] = arr[0]
        res = arr[0]
        
        for i in range(1, n):
            no_del[i] = max(no_del[i - 1] + arr[i], arr[i])
            one_del[i] = max(one_del[i - 1] + arr[i], no_del[i - 1])
            res = max(res, no_del[i], one_del[i])
        
        return res
