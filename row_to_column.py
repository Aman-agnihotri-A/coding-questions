A=[[1,2,3,4],
[5,6,7,0],
[9,2,0,4]]
x_col=[]
x_row=[]
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j]==0:
            x_row.append(i)
            x_col.append(j)
for i in range(len(A)):
    if i in x_row:
        for j in range(len(A[0])):
            A[i][j]=0
    else:
        for j in range(len(A[0])):
            if j in x_col:
                A[i][j]=0
print(A)