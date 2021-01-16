def main():
	

	# Program that reads a line and a substring. It should then display the number of
	# occurrence of the given substring in the line.

	# str1="hello my name is my"

	# print(str1.count("my"))

	string1="my name is myomy" #14 length #16 #16-2+1
								#length 16 #16-3+1
	string2="my"

	string2_length=len(string2)

	count=0

	string1_length=len(string1)

	for i in range(0,string1_length-string2_length+1):

		#substrings of length2
		j=i        #0, 1
		count_loop=0
		substring=""
		while(count_loop < string2_length): #0<2, 1<2, 2<2, 
			substring=substring+string1[j]	#my , y 	
			count_loop=count_loop+1         #1,2
			j=j+1							#2
		print(substring) #my, y 	
		if substring==string2: #==
				count=count+1	#1


	print(count)
		#substring=""

		




main()