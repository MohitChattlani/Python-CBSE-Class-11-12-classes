def main():
	#print("hello")
	# Write a program that reads a string and displays the longest substring of the given string
# having just the consonants.

	# str1="i love my countryddd"
	# n=len(str1)

	# substring=""
	# substring_length=0
	# max_substring=""
	# max_substring_length=0
	# #abc
	# for i in range(0,n): 
	# 	if (not(str1[i] in "aeiou")):
	# 		substring=substring+str1[i] # l,v, my c,ntryddd
	# 		substring_length=substring_length+1 #2,1,5,7
	# 	if(str1[i] in "aeiou" or i==n-1): #
	# 		if (max_substring_length < substring_length): #0<2,2<1,2<5,5<0,5<7
	# 			max_substring=substring   # l, my c,ntryddd
	# 			max_substring_length=substring_length #2,5,7
	# 		substring=""
	# 		substring_length=0
	# 	# print(max_substring)
	# 	# print(max_substring_length)


	# print(max_substring)    #bc,ntryddd
	# print(max_substring_length) #2,7


	#Write a program that inputs a line of text and prints its each word in a separate line. Also,
	#prints the count of words in the line.

	string1="Welcome to python programming"
	n=len(string1)
	word=""
	count=0
	for i in range(0,n):
		if (string1[i]==" "):
			print(word)  #Welcome,to,python
			word=""
			count=count+1 #1,2,3

		else:
			#making word
			word=word+string1[i] #Welcome,to


	print(word) #programming

	count=count+1 #4

	print(count)  #4



main()