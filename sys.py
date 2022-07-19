from __future__ import division
from psychopy import visual, event, core
import numpy as np
import matplotlib.pyplot as plt
import random
import math
win = visual.Window(size=(800, 800),fullscr=False, screen=1,color='black')
d0=-90 #gravity degree
d1=0 #calibration degree
d2=d0-180 #start compensation degree
r0=math.radians(d0)
r1=math.radians(d1)
r2=math.radians(d2) #degree to radians transformation
limit=0.5 #time duration
transition=(-0.5*math.cos(r0),+0.5*math.sin(r0)) #start transition offset
for i in range (10):
 vx=3#random.randint(0,300)/100
 vy=3#random.randint(0,300)/100 #randomrize initial velocity
 polygon = visual.ShapeStim(win=win,size=0.03,vertices='circle',lineColor='red',fillColor='red')
 #stimuli defination
 polygon1 = visual.Line(win=win,
 start=(vx*vy/10*math.cos(r0)-(vy*vy/10-5*(vy/10)**2)*math.sin(r0)+0.8*math.cos(r2),
     vx*vy/10*math.sin(r0)+(vy*vy/10-5*(vy/10)**2)*math.cos(r0)+0.8*math.sin(r2)), 
 end=(vx*vy/10*math.cos(r0)+0.5*math.sin(r1)-(vy*vy/10-5*(vy/10)**2)*math.sin(r0)+0.8*math.cos(r2),
     vx*vy/10*math.sin(r0)+(vy*vy/10-5*(vy/10)**2)*math.cos(r0)-0.5*math.cos(r1)+0.8*math.sin(r2)),
 lineColor='yellow', fillColor='yellow')
 #calibration defination
 start= visual.ShapeStim(win=win,size=0.03,vertices='circle',
 pos=[0.8*math.cos(r2),+0.8*math.sin(r2)],lineColor='red',fillColor='red')
 end= visual.ShapeStim(win=win,size=0.03,vertices='circle',
 pos=[vx*limit*math.cos(r0)-(vy*limit-5*limit**2)*math.sin(r0)+0.8*math.cos(r2),
     vx*limit*math.sin(r0)+(vy*limit-5*limit**2)*math.cos(r0)+0.8*math.sin(r2)],
     lineColor='blue',fillColor='blue')
 mark = visual.ShapeStim(win=win,size=0.03,vertices='circle',
 pos=[vx*vy/10*math.cos(r0)-(vy*vy/10-5*(vy/10)**2)*math.sin(r0)+0.8*math.cos(r2),
     vx*vy/10*math.sin(r0)+(vy*vy/10-5*(vy/10)**2)*math.cos(r0)+0.8*math.sin(r2)],
     lineColor='white',fillColor='white')
 #three marks definations
 t=0
 #trial loop
 while True:
    if event.getKeys('escape'):
     win.close()
    start.draw()
    if event.getKeys('left'):
     d1=d1-1
     r1=math.radians(d1)
     polygon1.end=(vx*vy/10*math.cos(r0)+math.sin(r1)-(vy*vy/10-5*(vy/10)**2)*math.sin(r0)+0.8*math.cos(r2),
     vx*vy/10*math.sin(r0)+(vy*vy/10-5*(vy/10)**2)*math.cos(r0)-math.cos(r1)+0.8*math.sin(r2))
    if event.getKeys('right'):
     d1=d1+1
     r1=math.radians(d1)
     polygon1.end=(vx*vy/10*math.cos(r0)+math.sin(r1)-(vy*vy/10-5*(vy/10)**2)*math.sin(r0)+0.8*math.cos(r2),
     vx*vy/10*math.sin(r0)+(vy*vy/10-5*(vy/10)**2)*math.cos(r0)-math.cos(r1)+0.8*math.sin(r2))
    if event.getKeys('space'):
     print(d1)
     break
    if vy-10*t<=0:
     polygon.fillColor='blue'
     polygon.lineColor='blue'
     mark.draw()
    if t<limit:
     t =0.001+t
     polygon.pos = (vx*t*math.cos(r0)-(vy*t-5*t**2)*math.sin(r0)+0.8*math.cos(r2),
     vx*t*math.sin(r0)+(vy*t-5*t**2)*math.cos(r0)+0.8*math.sin(r2))
     polygon.draw()
    if t>limit:
     end.draw()
    polygon1.draw()
    win.flip()
 #trial loop
win.close()
core.quit()


