s=["flower","flow","floo"]
f=s[0][0]
g=0

flag=1
for i in range(len(s[0])):
    for j in range(len(s)):
        print(g,i,j)
        if f[g]!=s[j][i]:
            break

        if flag==1 and j==len(s)-1:
            f+=s[j][i]
            g+=1
        if flag==0 and i==0:
            print("") 
    print(f)