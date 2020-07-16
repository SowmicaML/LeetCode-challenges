**********************************************************************

"""Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""
**********************************************************************
#using builtin function
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)
        
#recursive method without using builtin func        
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        if n==1: return x
        if n<0: return self.myPow(1/x,-n)
        result=self.myPow(x*x,n//2)
        if n%2==1: result*=x
        return result
        
            
        
