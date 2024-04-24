a="bobob"
count=0
for i in range(len(a)):
    if a[i]=='b':
        print(a[i+1:i+3])
        if i+2<len(a) and a[i+1:i+3]=='ob':
            count+=1
            print(count)