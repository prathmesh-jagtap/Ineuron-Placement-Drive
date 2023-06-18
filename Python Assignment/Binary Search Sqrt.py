"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator. 

 Example 1:
Input: x = 4 Output: 2 Explanation: The square root of 4 is 2, so we return 2.
"""
# Code:
def mySqrt(x):
  # base case
  if x == 0 or x == 1:
      return x
  
  l = 0  
  r = x/2 
  while l <= r:
      mid = (l+r)//2
  
      if mid*mid == x:
          return int(mid)
      elif mid*mid < x:
          l = mid + 1
          ans = mid
      else:
          r = mid - 1
  return int(ans)
