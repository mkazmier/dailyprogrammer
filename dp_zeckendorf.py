"""Challenge #74 [Easy]
   https://www.reddit.com/r/dailyprogrammer/comments/wa0mc/792012_challenge_74_easy/?"""

import time

def zeckendorf(n):
   '''Find the representation of a number as a sum of non-consecutive Fibonacci numbers'''
   fib = [0, 1]
   while fib[-1] <= n:
      fib.append(fib[-1] + fib[-2])
   
   res = []
   
   for f in fib[::-1]:
      if f <= n:
         res.append(f)
         n -= f 
   return res

t1 = time.perf_counter()
zeck = zeckendorf(10**100)
t2 = time.perf_counter() - t1
print("Result: {}\nElapsed time: {} ms".format(zeck, t2*1000))
