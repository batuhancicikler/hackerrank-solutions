# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:32:43 2019

@author: batuhan
"""

#Given an array of integers, find the sum of its elements

def simpleArraySum(ar):
    
    toplam = 0
    for i in ar:
        toplam += i
    return toplam