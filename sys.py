from __future__ import division
from psychopy import visual, event, core
import numpy as np
import matplotlib.pyplot as plt
import random
import math
file = open("D:\Text.txt","a")
win = visual.Window(units='pix',size=(1920, 1080),fullscr=1, screen=1,color='black')
d0=random.randint(-90,90)#0 #gravity degree
file.write(str(d0-90)+'\n')
d1=-90 #calibration degree
d2=d0-180 #start compensation degree
r0=math.radians(d0)
r1=math.radians(d1)
r2=math.radians(d2) #degree to radians transformation
limit=0.4 #time duration
transition=(-250*math.cos(r0),+250*math.sin(r0)) #start transition offset
g=10*500
h=0.5*g
for i in range (10):
 vx=random.randint(500,1500)
 vy=random.randint(500,1500)
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
 pos=[vx*limit*math.cos(r0)-(vy*limit-h*limit**2)*math.sin(r0)+400*math.cos(r2),
     vx*limit*math.sin(r0)+(vy*limit-h*limit**2)*math.cos(r0)+400*math.sin(r2)],
     lineColor=(255,0,255),fillColor=(255,0,255))
 mark = visual.ShapeStim(win=win,size=15,vertices='circle',
 pos=[vx*vy/g*math.cos(r0)-(vy*vy/g-h*(vy/g)**2)*math.sin(r0)+400*math.cos(r2),
     vx*vy/g*math.sin(r0)+(vy*vy/g-h*(vy/g)**2)*math.cos(r0)+400*math.sin(r2)],
     lineColor=(0,255,255),fillColor=(255,0,255))
 #three marks definations
 t=0
 #trial loop
 while True:
    border.draw()
    if event.getKeys('escape'):
     win.close()
    start.draw()
    if event.getKeys('left'):
     d1=d1-1
     r1=math.radians(d1)
     polygon1.pos=(500*math.cos(r1),500*math.sin(r1))
    if event.getKeys('right'):
     d1=d1+1
     r1=math.radians(d1)
     polygon1.pos=(500*math.cos(r1),500*math.sin(r1))
    if event.getKeys('space'):
     file.write(str(d1)+' ')
     break
    #if vy-g*t<=0:
     #polygon.fillColor=(255,0,255)
     #polygon.lineColor=(255,0,255)
     #mark.draw()
    if t<limit:
     t =0.001+t
     polygon.pos = (vx*t*math.cos(r0)-(vy*t-h*t**2)*math.sin(r0)+400*math.cos(r2),
     vx*t*math.sin(r0)+(vy*t-h*t**2)*math.cos(r0)+400*math.sin(r2))
     polygon.draw()
    polygon0.draw()
    polygon1.draw()
    win.flip()
 #trial loop
file.write('\n')
win.close()
core.quit()


