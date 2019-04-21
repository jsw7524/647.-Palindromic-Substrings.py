class Solution(object):
    def countSubstrings(self, s):
        if s == "":
            return 0
        count=0
        dp=[[0]*(len(s)) for i in range((len(s)))]
        dp[len(s)-1][len(s)-1]=1
        count += 1
        for i in range(len(s)-1):
            dp[i][i]=1
            count+=1
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                count += 1

        for i in range(2,len(s)):
            for j in range(i-1):
                if s[j] == s[i] and dp[j+1][i-1] == 1:
                    dp[j][i]=1
                    count+=1
        return count


sln =Solution()
assert 15==sln.countSubstrings("aaaaa")
assert 6==sln.countSubstrings("aaa")
assert 3==sln.countSubstrings("abc")
assert 10==sln.countSubstrings("aaaa")
assert 12==sln.countSubstrings("abcabcabcabc")
assert 35==sln.countSubstrings("bfdbvnjdfrkefndjfbfdbvnjdfrkefndjf")
assert 0==sln.countSubstrings("")
assert 1==sln.countSubstrings("a")