# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:32:13 2016

@author: manmeensaini
"""

def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
 # Now call the function we just defined:
     
fib(100)