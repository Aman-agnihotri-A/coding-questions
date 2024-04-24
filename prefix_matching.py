
class solution:
    def solve(self,A,B):
        l=[]
        for i in range(len(A)):
            
            if B in str(A[i]):
                c=A[i]
                if B== c[0:len(B)]:
                    print(A[i])
                    l.append(i)
        print(l)
        if len(l) ==0:
            return [-1,-1]
        elif len(l)==1:
            l.append(l[0])
            return l
        else:
            g=list()
            g.append(l[0])
            g.append(l[-1])
            return g
f=solution()
h=f.solve(["a","aa","aab","b","bb","bba"],"bb")
print(h)
