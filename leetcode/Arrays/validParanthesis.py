'''class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':0,')':0,'{':0,'}':0,'[':0,']':0}
        for i in range(len(s)):
                d[s[i]]+=1
        print(d)
        s=['(',')','{','}','[',']']
        for i in range(0,len(d.values()),2):
            if d[s[i]]!=d[s[i+1]]:
                return False
        return True'''
class Solution:
    def isValid(self, s: str) -> bool:
        f=[]
        for i in s:
            if i in '({[':
                f.append(i)
            else:
                #print(f)
        
                if(not f)or (i==')' and f[-1]!='(') or (i=='}' and f[-1]!='{') or(i==']' and f[-1]!='['):
                    
                    return "false"
        return "true"


    
print(Solution().isValid("(]"))

