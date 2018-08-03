#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:56:59 2017

@author: timo
"""
import random


class Dim:
  def __init__(self,n):
    self.n = n
#  def n(self):
#    return int(self.n)
  
d = Dim(3)

print(d.n)

print([0]*d.n)

class Space(Dim):
  def __init__(self,n):
    Dim.__init__(self,n)
    self.coordinates = [0]*n
    
s = Space(d.n)
print(s.coordinates,s.n)

class SpaceWalls(Space):
  def __init__(self,n,coordinates):
    Space.__init__(self,n)
    self.wallMin=coordinates
    self.wallMax=[10]*n
    
b = SpaceWalls(s.n,s.coordinates)    
print(b.n,b.coordinates,b.wallMax,b.wallMin)

class Obj(SpaceWalls):        
  def __init__(self,n,coordinates):
    SpaceWalls.__init__(self,n,coordinates)
    self.objCoordinates = coordinates.copy()
    self.hist = [coordinates.copy()]
  def goFwd(self,i):
    if i>=1 and i<= self.n:
      if self.objCoordinates[i-1]<self.wallMax[i-1]:
        self.objCoordinates[i-1] += 1
        self.hist.append(self.objCoordinates.copy())
      else :
        print("Can't go from maze through a wall")
    else: 
      print("Wrong dimension i")
  def goBwd(self,i):
    if i>=1 and i<= self.n:
      if self.objCoordinates[i-1]>self.wallMin[i-1]:
        self.objCoordinates[i-1] -= 1
        self.hist.append(self.objCoordinates.copy())
      else :
        print("Can't go from maze through a wall")
    else: 
      print("Wrong dimension i")
  def goBack(self,s):
    if s <= self.hist.index(self.objCoordinates):
      self.objCoordinates = self.hist[self.hist.index(self.objCoordinates)-s]
    else:
      print("too many steps back")

class Distance(Obj):
#  def __init__(self,n,coordinates):
#    Obj.__init__(self,n,coordinates)
#  
  def distance(self): 
    x = 0
    for h in self.objCoordinates:
      x += h
    for i in labpath.hist:
      y = 0
      n = 0
      for j in i:
        y += abs(self.objCoordinates[n]-j)
        n += 1
      if y<x and y>0:
        x = y
      else :
        x = x
    return x
        
  
o = Obj(s.n,s.coordinates)
print(o.n, o.coordinates)
print(o.n, o.coordinates, o.objCoordinates)
print(o.hist)

o.goFwd(2)
print(o.objCoordinates)
print(o.hist)

o.goFwd(3)
print(o.objCoordinates)
print(o.hist)

o.goFwd(4)
print(o.objCoordinates)

o.goBwd(1)

print(o.hist)

# create Map for labyrinth

labpath = Obj(s.n,s.coordinates)
print(labpath.coordinates,labpath.n
      ,labpath.wallMax,labpath.wallMin,labpath.objCoordinates)

i=0
while labpath.objCoordinates != labpath.wallMax:
  if random.random() <= 0.3:
    labpath.goBwd(random.randint(1,labpath.n))
  else:
    labpath.goFwd(random.randint(1,labpath.n))

print(labpath.objCoordinates)


print(len(labpath.hist))


labpath.goBack(10)

print(labpath.objCoordinates)

dist = Distance(labpath.n,labpath.objCoordinates)

print(dist.distance(),dist.hist)
print(labpath.hist)

print(dist.objCoordinates)

labpath.goBwd(2)
print(labpath.objCoordinates)

# create start position


# create end position


# create visualization of game


# game playing


# create code for automatic player


# possible ends -> catches + congratulations

