a=[[1,2,3,4],
[5,6,7,0],
[9,2,0,4]]
i_index,j_index=set(),set()
n=len(a)
m=len(a[0])
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            i_index.add(i)
            j_index.add(j)
print(i_index,j_index)
for i in range(n):
    for j in range(m):
        if i in i_index or j in j_index:
            a[i][j]=0
print(a)
