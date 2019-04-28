# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:25:03 2019

@author: batuhan
"""

# Given an array of integers, calculate the fractions of its elements that are positive, 
# negative, and are zeros. Print the decimal value of each fraction on a new line.

def plusMinus(arr):
    neg = 0
    pos = 0
    zero = 0
    for i in range(0, len(arr)):
        if arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
        else:
            zero += 1
    print(format(pos / n, ".6f"))
    print(format(neg / n, ".6f"))
    print(format(zero / n, ".6f"))
    