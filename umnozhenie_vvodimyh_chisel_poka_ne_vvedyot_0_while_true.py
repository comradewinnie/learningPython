c=0
a=int(input("введи число: "))
b=1
c=a*b
while True:
	a=int(input("введи число: "))
	c=c*a
	if a<=0: break
	print(c)