import functools
def factors(item):
    count=0
    x=int(item**0.5)+1
    for i in range(1,x):
        if item%i==0:
            count+=1
    return count
def comparator(a,b):
    if factors(a)<factors(b):
        return 1
    elif factors(a)>factors(b):
        return -1
    elif factors(a)==factors(b):
        if a<b:
            return 1
        else:
            return -1
def compute(a):
    x=sorted(a,key=functools.cmp_to_key(comparator),reverse=True)
    return x
a=[1,6,9,4,13]
print(compute(a))

