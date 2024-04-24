class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        sum=0
        
        while mainTank>=0:
            if mainTank<5:
                return (mainTank*10)+(sum*50)
            if additionalTank>0:
                additionalTank-=1
                mainTank=mainTank-5+1
                sum+=1
                if mainTank==0:
                    return sum
print(Solution().distanceTraveled(9,1))