from operator import itemgetter
import math


flag=True
rides=[]
cars=[]
available=[]
busy=[]
match={}

i=0

with open('example.in') as fileInput:
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
i=0
for i in range(F):
	available.append([i,0,0,-1])
	match[i]=[]

	i+=1
rides = sorted(rides, key=itemgetter(6))
for i in range(T):
	# available cars
	flag=True
	while(flag==True):
		if (busy==[]):
			flag=False
		else:
			print(busy)
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
			minDistance=-math.inf
			minIndex=0
			for k in available:
				dist=abs(j[1]-k[1])+abs(j[2]-k[2])
				if (dist<minDistance):
					minDistance=dist
					minIndex=k[0]
			match[minIndex].append(j[0])
			waitTmp=j[5]-(dist+i)
			if (waitTmp<0): waitTmp=0
			endTime=i+dist+waitTmp+abs(j[3]-j[1])+abs(j[4]-j[2])

			# delete from available minIndex
			for l in available:
				if l[0]==minIndex:
					available.remove([minIndex,l[1],l[2],l[3]])

			# add car to busy
			busy.append([minIndex,j[3],j[4],endTime])
			busy=sorted(busy,key=itemgetter(3))

			# pop ride
			del(rides[0])
print(match)









    		
