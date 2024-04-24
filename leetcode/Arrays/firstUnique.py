f={}
s="leetcode"
g=[]

for i in range(len(s)):
    if s[i] in f:
        if s[i] in g:
            g.remove(s[i])
    else:
        f[s[i]]=i
        g.append(s[i])
print(g)
if g:
    print(f[g[0]])
else:
    print(False)