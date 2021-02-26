#! /usr/bin/env python3
# coding=utf-8
import pytest
def Fibonacci(n):
    if n<0:
        print("No")
    elif n==1:
        return 1
    elif  n==0:
        return 0
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
def factorial(m):
    fac=1
    for i in range(1,m+1):
        fac=fac*i
    return fac
class Testclass:
    def test_a(self):
        assert Fibonacci(2) == 1
        assert Fibonacci(1) == 1
        assert Fibonacci(0) == 0
    def test_b(self):
        assert Fibonacci(-1) == None
        assert Fibonacci(6) == 8
    def test_c(self):
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
if __name__=='__main__':
    pytest.main(["-s","Fibonacci.py"])