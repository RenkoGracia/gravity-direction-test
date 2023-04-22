from __future__ import division
from psychopy import visual, event, core
import numpy as np
import matplotlib.pyplot as plt
import random
import math
file = open("D:\Text.txt","a")
win = visual.Window(units='pix',size=(1920, 1080),fullscr=1, screen=1,color='black')
win.mouseVisible=False
for j in range (16):
 d0=j*157.5#random.randint(-1,4)*60 #gravity degree
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
 limit=0.3 #time duration
 transition=(-250*math.cos(r0),+250*math.sin(r0)) #start transition offset
 g=7050
 h=0.5*g
 for i in range (10):
  vx=(random.randint(0,1)*2-1)*random.randint(200,800)
  vy=random.randint(int(1.6*abs(vx))-1800,int(-1.5*abs(vx))+3800)
  print(vx,vy)
 #randomrize initial velocity
  polygon = visual.ShapeStim(win=win,size=15,vertices='circle',lineColor=(0,255,255),fillColor=(0,255,255))
 #stimuli defination
  border = visual.ShapeStim(win=win,size=1000,vertices='circle',lineColor=(255,0,255))
  polygon0= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[0,0],lineColor=(255,0,255),fillColor=(255,0,255))
  polygon1= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[500*math.cos(r1),500*math.sin(r1)],lineColor=(255,0,255),fillColor=(255,0,255))
 #calibration defination
  start= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[0,0],lineColor=(0,255,255),fillColor=(0,255,255))
  end= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[vx*limit*math.cos(r0)-(vy*limit-h*limit**2)*math.sin(r0)-vx*vy*math.cos(r0)/g+(0.15*vy-0.15*vx-120)*math.sin(r0),
     vx*limit*math.sin(r0)+(vy*limit-h*limit**2)*math.cos(r0)-vx*vy*math.sin(r0)/g-(0.15*vy-0.15*vx-120)*math.cos(r0)],
     lineColor=(0,255,255),fillColor=(0,255,255))
 #three marks definations
  timer = core.CountdownTimer(0.32)
 #trial loop
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
      while d1-d0>90:
       d1=d1-360
      while d1-d0<-270:
       d1=d1+360
      file.write(str(d1)+',')
      break
    #if vy-g*t<=0:
     #polygon.fillColor=(255,0,255)
     #polygon.lineColor=(255,0,255)
     #mark.draw()
    if 0>t:
     polygon.pos = (-vx*vy*math.cos(r0)/g+(0.15*vy-0.15*vx-120)*math.sin(r0),-vx*vy*math.sin(r0)/g-(0.15*vy-0.15*vx-120)*math.cos(r0))
     polygon.draw()
    if 0<t<limit:
     polygon.pos = (vx*t*math.cos(r0)-(vy*t-h*t**2)*math.sin(r0)-vx*vy*math.cos(r0)/g+(0.15*vy-0.15*vx-120)*math.sin(r0),
     vx*t*math.sin(r0)+(vy*t-h*t**2)*math.cos(r0)-vx*vy*math.sin(r0)/g-(0.15*vy-0.15*vx-120)*math.cos(r0))
     polygon.draw()
    if 0.31>t>limit:
     end.draw()
    polygon0.draw()
    polygon1.draw()
    win.flip()
 #trial loop
 file.write('\n')
win.close()
core.quit()
