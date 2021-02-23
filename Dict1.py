def main():
	#Write a program to read roll numbers and marks of four students and create a directory
	#from it having roll numbers as keys.

	#arr[0]=1
	#dict1['key']=value
	roll_marks={}

	for i in range(0,4):
		rno=eval(input("enter roll no"))
		marks=eval(input("enter marks"))
		roll_marks[rno]=marks

	print(roll_marks)

main()