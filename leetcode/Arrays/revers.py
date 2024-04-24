def f(x):
    x=str(x)
    return True if x==int(x[::-1]) else False
s=12
print(f(s))