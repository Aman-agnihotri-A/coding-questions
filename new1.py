a=int(input())
h=''
g=0
while a>0:
    h+=chr(((a-1)%26)+65)
    a=(a-1)//26
    print(g)
    
print(h)