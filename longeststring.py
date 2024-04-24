'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        count=0
        g=0
        i=0
        l=[]
        p=''
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        while i<len(s):
            if s[i] in d:
                print(s[i])
                l.append(count)
                print(p)
                i=d[s[i]]+1
                p=''
                d={}
                count=0
                i=i
                
            else:
                d[s[i]]=i
                print(d)
                p+=s[i]
                i+=1
                count+=1
                if i==len(s):
                    print(p)
        l.append(count)
        print(l)
        return max(l)'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                print(charMap)
                left = charMap[s[right]] + 1
                print(left)
                charMap[s[right]] = right
        
        return maxLength
print(Solution().lengthOfLongestSubstring('dvdf'))