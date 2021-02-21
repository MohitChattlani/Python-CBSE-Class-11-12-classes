def main():

	#Converting integer number to list
	x=123
	quotient=x
	list1=[]
	while(quotient>0):
		rem=quotient%10    #3,2,1
		list1.append(rem) #[3,2,1]
		quotient=int(quotient/10)

	print(list1)

main()