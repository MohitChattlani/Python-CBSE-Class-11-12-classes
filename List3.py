def main():
	
	#Program to find the minimum element from a list of 
	#element along with its index in the
 	#list.

 	list1=[8,7,1,0,9]

 	minimum=list1[0]  #8
 	minindex=0 		  #0

 	l=len(list1)
 	for i in range(1,l):
 		#condition if the coming element is min
 		if (list1[i]<minimum):  #7<8,1<7,0<1,9<0
 			minimum=list1[i]    #7,1,0
 			minindex=i 			#1,2,3

 	print(minimum)

 	print(minindex)


main()