import numpy as np
import matplotlib.pyplot as plt
import random
import math
x=[]
y=[]
d=60 #set rotation degrees
print(d,' degrees')
r=math.radians(d) #transform into radians
for j in range(3):#set graph amount
 width=random.uniform(0,3) #select graph width
 if width<1: #narrow width
  a=random.uniform(0.5,2)
  print('narrow')
 elif width>2: #middle width
  a=random.uniform(4,8)
  print('middle')
 else: #wide width
  a=random.uniform(2,4)
  print('wide')
 lr=random.uniform(-1,1) #set starting side
 if lr<0:
  print('left')
 else:
  print('right')
 sd=random.uniform(-1,1) #set side amount
 if sd<0:
  dx=0 #always set (0,0) vertex
  print('single side')
 else:
  dx=random.uniform(10/3,5*3**0.5-5) #set random end point
  print('double side')
 for i in range (100): #run animation
  if lr>0: #right side
   t=(10-0.1*i-dx)*a
  else: #left side
   t=(0.1*i+dx-10)*a
  x.append(t*math.cos(r)+t**2*math.sin(r)/a**2) #x value after rotation
  y.append(t*math.sin(r)-t**2*math.cos(r)/a**2) #y value after rotation
  plt.axis([-120,120,-120,120]) #adjust axis size on a
  plt.plot(x,y) #draw graph
  plt.pause(0.001) #draw speed
 x.clear() #reset x
 y.clear() #reset y
 plt.pause(3) #reserve graph for 3 s
 print()
 if j!=2: #clear previous graph except the last one
  plt.clf()
plt.show() #reserve final graph