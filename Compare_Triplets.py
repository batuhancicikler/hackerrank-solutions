# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:42:41 2019

@author: batuhan
"""

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(0, len(a)):
        if a[i] > b[i]: 
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice, bob
        