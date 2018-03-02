from operator import itemgetter
import math
import functools
import numpy as np
import sys

w1 = 0.5

flag=True
rides=[]
cars=[]
available=[]
busy=[]
match={}

i=0

with open(sys.argv[1] + '.in') as fileInput:
    for line in fileInput:
    	inp=[int(x) for x in line.split(' ')]
    	if (flag==True):
    		R=inp[0]
    		C=inp[1]
    		F=inp[2]
    		N=inp[3]
    		B=inp[4]
    		T=inp[5]
    		flag=False
    	else:
    		rides.append([i]+inp)
    		i+=1

minimum, maximum = math.inf, -math.inf
minimumTime, maximumTime = math.inf, -math.inf
for a in rides:
    minimum = min(minimum, (abs(a[4] - a[2]) + abs(a[3] - a[1])) )
    maximum = max(maximum, (abs(a[4] - a[2]) + abs(a[3] - a[1])) )
    minimumTime = min(minimumTime, a[6])
    maximumTime = max(maximumTime, a[6])



for i in range(F):
	available.append([i,0,0,-1])
	match[i]=[]
if minimumTime == maximumTime:
    minimumTime = 0

rides = sorted(rides, key= lambda a :  w1 * ( 1 -  (abs(a[4] - a[2]) + abs(a[3] - a[1]) - minimum) / (maximum - minimum) )  + (1 - w1) *  (a[6] - minimumTime) / (maximumTime - minimumTime))

for i in range(T):
	# available cars
	flag=True
	while(flag==True):
		if (busy==[]):
			flag=False
		else:
			# print(busy)
			if (busy[0][3]<=i):
				available.append(busy[0])
				del(busy[0])
			else:
				flag=False
	flag2=True

	# match table cars
	while (flag2==True):

		if (available==[] or rides==[]):
			flag2=False
		else:
			j=rides[0]
			minDistance=math.inf
			minIndex=0
			counter=0
			for t,k in enumerate(available):
				dist=abs(j[1]-k[1])+abs(j[2]-k[2])
				if (dist<minDistance):
					minDistance=dist
					minIndex=k[0]
					counter=t
			match[minIndex].append(j[0])
			waitTmp=j[5]-(dist+i)
			if (waitTmp<0): waitTmp=0
			endTime=i+dist+waitTmp+abs(j[3]-j[1])+abs(j[4]-j[2])

			# delete from available minIndex
			available.pop(counter)

			# add car to busy
			busy.append([minIndex,j[3],j[4],endTime])
			busy=sorted(busy,key=itemgetter(3))


			# pop ride
			del(rides[0])
	# print(busy)
	# print(available)
for i,j in match.items():
	print(str(len(j))+' '+' '.join([str(x) for x in j]))
