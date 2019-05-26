def delay(filename):
	x= open(filename)
	rx=[]
	Avg=[]
	c=[]
	for line in x:
		if 'Rx Packets' in line:
			line = line.split(" ")
			rx.append(int(line[6]))
		elif 'mean Delay' in line:
			line = line.split(" ")
			Avg.append(float(line[2]))
	sm = 0
	n = 0
	for i in range(len(rx)):
		n += rx[i] 
		if rx[i] != 0:
			sm += (Avg[i] * rx[i])
	avgsum = float(sm/n)
	print("Average Delay = ", str(avgsum) + "ms" )
	
	for i in Avg:
		if i != '-nan':
			c.append(i)
	
	maximum = max(c)
	print("Maximum Delay = ", str(maximum) + "ms")	

d = delay('Project2_Flows.txt')
	
	
