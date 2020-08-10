class Solution:
    def fib(self, N: int) -> int:
        
        if N <= 1:
            return N
        
        fib = [0] * (N+1)
        
        fib[0], fib[1] = 0, 1
        
        for i in range(2, N+1):
            fib[i] = fib[i-2] + fib[i-1]
            
        return fib[N]
        
        
        
        
        