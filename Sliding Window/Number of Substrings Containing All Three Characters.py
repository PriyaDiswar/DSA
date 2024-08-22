"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 """

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l,r=0,0
        res=0
        n=len(s)
        d={"a":0,"b":0,"c":0}
        while l+3<=n:
            if d["a"]>=1 and d["b"]>=1 and d["c"]>=1:
                res+=(n-r+1)
                d[s[l]]-=1
                l+=1
            else:
                if r<n:
                    d[s[r]]+=1
                    r+=1
                else:
                    break
        return res
        
