class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
    
            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):
    
                # Update all multiples of p
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        
        # Print all prime numbers
        print(prime)
        a=[]
        for p in range(2, n+1):
            if p<=(n//2):
                if prime[p] and prime[n-p]:
                    a.append([p,n-p])
        return a
print(Solution().findPrimePairs(10))