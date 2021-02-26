#! /usr/bin/env python3
# coding=utf-8
import unittest
from Fibonacci import*
class TestCase(unittest.TestCase):
    def test_Fibonacci(self):
        self.assertEqual(Fibonacci(-1),None)
        self.assertEqual(Fibonacci(0),0)
        self.assertEqual(Fibonacci(1),1)
        self.assertEqual(Fibonacci(2),1)
        self.assertEqual(Fibonacci(3),2)
        self.assertEqual(Fibonacci(6),8)
    def test_factorial(self):
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(1),1)

if __name__=='__main__':
    unittest.main()

