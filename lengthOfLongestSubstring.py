class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counterdict = {}
        substring = ''
        for i in range(len(s)):
            if s[i] not in substring:
                substring += s[i]
            else:
                substring = substring[substring.index(s[i])+1:]+s[i]
            counterdict[substring] = len(substring)
        return (max(counterdict.values()) if substring else 0)
                