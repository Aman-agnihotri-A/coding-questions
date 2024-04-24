a=int(input())
b=int(input())
s=''
while a>0:
    s+=str(a%b)
    a=a//b
print(s[::-1])