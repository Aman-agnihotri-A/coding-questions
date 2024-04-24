s="-123"
if int(s)<0:
    p=s[0]
    s=s[1:]
    print(int(p+s[::-1]))
#print(int(s[::-1]))