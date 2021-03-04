def main():

	#Using fromkeys() method

	# x = ('key1', 'key2', 'key3')
	# y = 0

	# thisdict = dict.fromkeys(x, y)
	# print(thisdict)


	#Your school has declared to deposit scholarship amount of Rs. 2500/- 
	#to some selected students. Write a program to input the selected students’ 
	#roll number and create a dictionary for the same.


	rno_amt={}

	N=int(input("How many students"))

	scholarship_amt=2500

	for i in range(0,N):
		rno=int(input("Enter roll no:"))

		rno_amt[rno]=scholarship_amt


	print(rno_amt)


main()