def main():


	#Write a program that asks the user to input a number / 
	#a list to be appended to an
	#existing list. Whether the user enters a single number or a list of numbers, the
	#program should append the list accordingly

	list1=[1,2,3]
	print("Old list")
	print(list1)
	user_input=input("Enter list/number:")

	print(user_input)

	#this will give us true mathematical data structure
	user_input_mod=eval(user_input)

	print(user_input_mod)

	#if user gives integer
	if (type(user_input_mod)==type(1)):
		list1.append(user_input_mod)
	#if user gives list
	elif (type(user_input_mod)==type([])):
		list1.extend(user_input_mod)


	print("Final list")

	print(list1)

	




main()