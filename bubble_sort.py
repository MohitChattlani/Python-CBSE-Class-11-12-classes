def main():

	#Program to sort a list using Bubble sort

	list1=[7, 4, 2, 9, 20]
	print("Orignal list")
	print(list1)

	passes=len(list1)
	n=len(list1)

	for i in range(0,passes):
		print("Pass")
		print(i+1)

		for j in range(0,n-1):        #0,1,2
			if (list1[j]>list1[j+1]): #90>89,90>99,99>90
				#swapping code
				temp=list1[j] #90
				list1[j]=list1[j+1]   #89
				list1[j+1]=temp       #89,90,90,99

		print(list1)
		
	print("Sorted List")

	print(list1)



main()