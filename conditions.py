def main():
	pass
	print("abc")
	print("def")
	a=20
	a=5
	if (a>10):
		print("hello")
	else:
		print("not hello")

	print("next statement")

	i=1
	while(i<10): #1<10 #2<10
		print(i) #1,2,3,...9
		i=i+1 #i=1+1,i=2+1,i=10

	print("end of loop")

	a=10
	b=7
	c=15

	if a>b and a>c:
		print("Max is",a)
	if b>a and b>c:
		print("Max is",b)
	if c>a and c>b:
		print("Max is",c)

	a=10
	if (a>30):
		if (a>40):
			print("a>40")
		else:
			print("a<40")
	elif(a>15):
		if (a>25):
			print("a>25")
		else:
			print("a<25")
	else:
		if (a>12):
			print("a>12")
		else:
			print("a<12")

	print("Out of Conditioning")


main()