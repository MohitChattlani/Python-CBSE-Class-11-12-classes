def main():

	#Consider a directory Stud that stores rollno and marks. 
	#Write a program to input a rollno and delete it from the dictionary. 
	#Display error message if the rollno does not exists in the dictionary.


	dict1={1:90,2:85,3:90}

	rno=int(input("Enter rollno:"))

	if (rno in dict1):
		del dict1[rno]
		print("Deleted")

	else:
		print("Key not found")

	#value=dict1.pop(rno,"Not Found")
	#print(value)
	print("Final dictionary")
	print(dict1)
main()