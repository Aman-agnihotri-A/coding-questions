class Solution:
    def solve(self,A):
        n=len(A)
        x=n-1
        preeven=[0]*n
        preodd=[0]*n
        sufeven=[0]*n
        sufodd=[0]*n
        #print(preeven)
        if x==0:
            return 0
        for i in range(len(A)):
            if i%2==0:
                if i!=0:
                    preeven[i]=A[i]+preeven[i-1]
                    sufeven[x-i]=A[x-i]+sufeven[x-i+1]
                    
                    preodd[i]=preodd[i-1]
                    sufodd[x-i]=sufodd[x-i+1]
                else:
                    preeven[i]+=A[i]
                    sufeven[x-i]+=A[x-i]
            else:
                preodd[i]=A[i]+preodd[i-1]
                sufodd[x-i]=A[x-i]+sufodd[x-i+1]
                
                preeven[i]=preeven[i-1]
                #print(preeven[i])
                sufeven[x-i]=sufeven[x-i+1]
        #print(preeven,sufeven,"\n",preodd,sufodd)
        count=0
        h=[]
        #print(x)
        if x%2==1:
            h=sufeven
            sufeven=sufodd
            sufodd=h
            print(preeven,sufeven,"\n",preodd,sufodd)
        for i in range(len(A)):
            if i==0:
                if sufeven[i+1]==sufodd[i+1]:
                    count+=1
            elif i==x:
                if preeven[i-1]==preodd[i-1]:
                    count+=1
            else:
                if preeven[i-1]+sufodd[i+1]==preodd[i-1]+sufeven[i+1]:
                    count+=1
        return count



print(Solution().solve([5,5]))