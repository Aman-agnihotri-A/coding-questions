a=int(input())
g=[[1,2,3],[1,2,3],[1,2,3]]

top=0
bottom =a-1
left=0
right=a-1
print(right)
d=0
x=1
while(top<=bottom and left<=right):
    if d==0:
        for i in range(left,right+1):

            g[top][i]=x
            x+=1
        top+=1
        d=1
    print(g)
    if d==1:
        for i in range(top, bottom+1):
            g[i][right]=x
            x+=1
        right-=1
        d=2
    if d==2:
        for i in range(right,left-1,-1):
            g[bottom][i]=x

            x+=1
        bottom-=1
        d=3
    if d==3:
        for i in range(bottom,top-1,-1):
            g[i][left]=x
            x+=1
        left+=1
        d=0
for i in range(3):
    print(g[i],end=" \n")
