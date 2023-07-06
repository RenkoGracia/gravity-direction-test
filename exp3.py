from __future__ import division
from psychopy import visual, event, core
import numpy as np
import matplotlib.pyplot as plt
import random
import math
objnum=10
file = open("D:\Text.txt","a")
win = visual.Window(units='pix',size=(1920, 1080),fullscr=1, screen=1,color='black')
win.mouseVisible=False
for j in range (24):
 d0=j*?#random.randint(-1,4)*60 #gravity degree
 while d0>270:
       d0=d0-360
 while d0<=-90:
       d0=d0+360
 file.write(str(d0-90)+'\n')
 d1=-90 #calibration degree
 d2=d0+90 #start compensation degree
 r0=math.radians(d0)
 r1=math.radians(d1)
 r2=math.radians(d2) #degree to radians transformation
 limit = 1
 #time duration
 g=7050
 h=0.5*g
 for i in range (30):
  stimuli=[]
  v=[]
  start=[]
  end=[]
  for j in range(objnum):
   vx=(random.randint(0,1)*2-1)*random.randint(200,800)
   vy=random.randint(-3000,3000)

   #randomrize initial velocity
   x=random.randint(-800,800)
   y=random.randint(-800,800)
   v.append((vx,vy,x,y))
   polygon = visual.ShapeStim(win=win,size=15,vertices='circle',lineColor=(0,255,255),fillColor=(0,255,255))
   stimuli.append(polygon)
   endpoint= visual.ShapeStim(win=win,size=15,vertices='circle',
   pos=[vx*limit*math.cos(r0)-(vy*limit-h*limit**2)*math.sin(r0)+v[j][2],
     vx*limit*math.sin(r0)+(vy*limit-h*limit**2)*math.cos(r0)+v[j][3]],
     lineColor=(0,255,255),fillColor=(0,255,255))
   end.append(endpoint)
 #stimuli defination
  border = visual.ShapeStim(win=win,size=1000,vertices='circle',lineColor=(255,0,255))
  polygon0= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[0,0],lineColor=(255,0,255),fillColor=(255,0,255))
  polygon1= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[500*math.cos(r1),500*math.sin(r1)],lineColor=(255,0,255),fillColor=(255,0,255))
 #calibration defination
  start= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[0,0],lineColor=(0,255,255),fillColor=(0,255,255))
 #trial loop
  timer=core.CountdownTimer(0.32)
  while 0.32-timer.getTime()>0:
    t=0.31-timer.getTime()
    border.draw()
    start.draw()
    if event.getKeys('escape'):
     win.close()
     file.write('\n')
    if event.mouseWheelRel[1]<0:
      d1=d1-1
      r1=math.radians(d1)
      polygon1.pos=(500*math.cos(r1),500*math.sin(r1))
      event.mouseWheelRel[1]=0
    if event.mouseWheelRel[1]>0:
      d1=d1+1
      r1=math.radians(d1)
      polygon1.pos=(500*math.cos(r1),500*math.sin(r1))
      event.mouseWheelRel[1]=0
    if event.mouseButtons[0]==1:
      event.mouseButtons[0]=0
      if (i+1)%3==0:
        while d1-d0>90:
         d1=d1-360
        while d1-d0<-270:
         d1=d1+360
        file.write(str(d1)+',')
      break
    if 0>t:
     for j in range(objnum):
      stimuli[j].pos =(v[j][2],v[j][3])
      stimuli[j].draw()

    if 0<t<0.3:
     for j in range(objnum):
      stimuli[j].pos =(v[j][0]*t*math.cos(r0)-(v[j][1]*t-h*t**2)*math.sin(r0)+v[j][2],
      v[j][0]*t*math.sin(r0)+(v[j][1]*t-h*t**2)*math.cos(r0)+v[j][3])
      stimuli[j].draw()
    if t>0.3:
     for j in range(objnum):
      end[j].draw()
    polygon0.draw()
    polygon1.draw()
    win.flip()
 #trial loop
 file.write('\n')
win.close()
core.quit()
