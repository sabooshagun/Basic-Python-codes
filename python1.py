def average(x):
	sum=0
	n=0
	for i in range (0,len(x)):
		if (isinstance(x[i],(float,int))):
			sum=sum+x[i]
			n=n+1
	if n==0:
		return None
	else:
		average= sum/n
		return average

print (average([1,2,4,5]))


def power(x,y):
	for i in range(0,len(x)):
		for j in range(0,len(y)):
			power=x[i]**y[j]
	return power

print(power([2],[5]))


def cd(x):
	for i in range(0,len(x)):
		cd= x[i]-x[i-1]
	return cd
print(cd([2,4,6,8]))

def area(x,y,a,b):
	for i in range(0,len(x)):
		for j in range(0,len(y)):
			d1= x[i]-y[i]
	for k in range(0,len(a)):
		for k in range(0,len(b)):
			d2= a[i]-b[i]
	area= d1*d2
	return area

print(area([30],[20],[10],[5]))
