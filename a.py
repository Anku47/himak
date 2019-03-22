n=3
pcheck=0
for i in range(2,n):
	if n%i==0:
		pcheck=1
	if pcheck==0:
		print(n)