#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:55:26 2018

@author: timo
"""

import sys
import math

class Player:
    def __init__(self,position,dim):
        self.position= position
        self.dim = dim

    def go_f(self,i):
        self.position[i] += 1

    def go_b(self,a):
        self.position[a] -= 1
       
p=Player([0,0,0],3)
print(p.dim)
print(p.position)
p.go_f(1)
print(p.position)