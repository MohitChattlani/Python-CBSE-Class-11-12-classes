def main():
	pass
	print("hello")

	sum=0
	for i in range(1,11):
		sum=sum+i
		print(sum)
		pass
	print(sum)

	fact=1

	for i in range(1,5):
		fact=fact*i

	print(fact)	

	sign=-1
	for i in range(5,26,5):
		num=i*sign #-5,10,-15
		print(num)
		sign=sign*-1 #1,-1

	for i in range(1,10):
		if i==8:
			break
		print(i)

	x=int(input())

	y=True
	for i in range(2,int(x/2)+1):
		if (x%i==0):
			y=False
			break			
	if (y):
		print("Prime")
	else:
		print("Not Prime")

	for i in range(1,10):
		if i==2:
			continue
		print(i)
		

	print("Out of for loop")

main()