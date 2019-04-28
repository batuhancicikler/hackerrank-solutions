# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:16:22 2019

@author: batuhan
"""

# given a square matrix, calculate the absolute difference between the sums of its diagonals

def diagonalDifference(arr):
    sayı1 = sum(arr[i][i] for i in range(n))
    sayı2 = sum(arr[i][n - i - 1] for i in range(n))
    return abs(sayı1 - sayı2)