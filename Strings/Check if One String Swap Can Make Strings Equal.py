"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""



class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt=0
        i=-1
        j=-1
        for _ in range(len(s1)):
            if s1[_]!=s2[_]:
                cnt+=1
                if i==-1:
                    i=_
                elif j==-1:
                    j=_
        if cnt==0:
            return True
        elif cnt==2 and s1[i]==s2[j] and s1[j]==s2[i]:
            return True
        return False
