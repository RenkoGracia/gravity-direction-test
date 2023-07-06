from __future__ import division
from psychopy import visual, event, core
import numpy as np
import matplotlib.pyplot as plt
import random
import math
file = open("D:\Text.txt","a")
win = visual.Window(units='pix',size=(1920, 1080),fullscr=1, screen=1,color='black')
win.mouseVisible=False
for j in range (24):
 #j=j+6
 d0=j*165
 while d0>270:
       d0=d0-360
 while d0<=-90:
       d0=d0+360
 file.write(str(d0-90)+'\n')
 d1=-90 #calibration degree
 r0=math.radians(d0)
 r1=math.radians(d1)
 limit=0.8 #time duration
 g=7050
 h=0.5*g
 for i in range (12):
  vx=(random.randint(0,1)*2-1)*300
  vy=random.randint(0,2)*800+2020#vy=2020/2820/3620
 #randomrize initial velocity
  polygon = visual.ShapeStim(win=win,size=15,vertices='circle',lineColor=(0,255,255),fillColor=(0,255,255))
 #stimuli defination
  border = visual.ShapeStim(win=win,size=1000,vertices='circle',lineColor=(255,0,255))
  polygon0= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[0,0],lineColor=(255,0,255),fillColor=(255,0,255))
  polygon1= visual.ShapeStim(win=win,size=15,vertices='circle',
  pos=[500*math.cos(r1),500*math.sin(r1)],lineColor=(255,0,255),fillColor=(255,0,255))
 #calibration defination
  timer = core.CountdownTimer(2.02)
 #trial loop
  while 2.02-timer.getTime()>0:
    t=2.01-timer.getTime()
    border.draw()
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
    if event.mouseButtons[2]==1:
      event.mouseButtons[2]=0
      d1=d1-90
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
     polygon.pos = (-vx*vy*math.cos(r0)/g+(0.4*vy-1008)*math.sin(r0),-vx*vy*math.sin(r0)/g-(0.4*vy-1008)*math.cos(r0))#change with vy
     polygon.draw()
    if 0<t<limit:
     polygon.pos = (vx*t*math.cos(r0)-(vy*t-h*t**2)*math.sin(r0)-vx*vy*math.cos(r0)/g+(0.4*vy-1008)*math.sin(r0),
     vx*t*math.sin(r0)+(vy*t-h*t**2)*math.cos(r0)-vx*vy*math.sin(r0)/g-(0.4*vy-1008)*math.cos(r0))
     polygon.draw()

    polygon0.draw()
    polygon1.draw()
    win.flip()
 #trial loop
 file.write('\n')
win.close()
core.quit()