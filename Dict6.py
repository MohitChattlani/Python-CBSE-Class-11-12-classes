def main():
	#Write a program to delete the keys of a dictionary, one by one 
	#in LIFO order. Make sure that there is no error generated after 
	#the last item deleted.

	numbers ={1:111, 2:222, 3:333, 4:444}
	print(numbers)
	mod_numbers=numbers

	# while (mod_numbers):    #{}
	# 	mod_numbers.popitem()
	# 	print(mod_numbers)


	# #loop here

	# print(mod_numbers)

	for i in range(0,len(mod_numbers)):
		mod_numbers.popitem()
		print(mod_numbers)

	#print(numbers)

main()