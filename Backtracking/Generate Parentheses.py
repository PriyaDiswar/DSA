"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(open,close,s):
            if len(s)==2*n:
                res.append(s)
                return
            if open<n:
                generate(open+1,close,s+"(")
            if close<open:
                generate(open,close+1,s+")")
        res=[]
        generate(0,0,"")
        return res
