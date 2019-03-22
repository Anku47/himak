a=2
count=0
while count<=9:
	c=0
	for i in range (2,a-1):
		if a%i==0:
			c=1
	if c==0:
		print(a)
		count=count+1
	a=a+1