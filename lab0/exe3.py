#!/usr/bin/python

hour = 6
minute = 52
second = 0

minute = minute + (8 * 1) + (7 * 3) + (8 * 1)
second = second + (15 * 1) + (12 * 3) + (15 * 1)

#print str(hour) + ':' + str(minute)

if(second >= 60):
    hp = (second/60)
    minute = minute + hp
    second = second - (hp *60)

if(minute >= 60):
    hp = (minute/60)
    hour = hour + hp
    minute = minute - (hp *60)


zh = ''
zm = ''
zs = ''
if(hour<10):
    zh=0
if(minute<10):
    zm=0
if(second<10):
    zs=0
    

print 'Time get home for breakfast: ' + \
    str(zh) + str(hour) + ':' +\
    str(zm) + str(minute) + ':' +\
    str(zs) + str(second)
