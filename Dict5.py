def main():
	
	#Write a program to read a sentence and then create 
	#a dictionary contains the frequency of letters digits 
	#in the sentence. Ignore other symbols, if any.

	alpha_digits ='abcdefghijklmnopqrstuvwxabcdefghijkl0123456789'

	frequency={}

	for i in range(0,len(alpha_digits)):
		character=alpha_digits[i]
		if (character in frequency):
			frequency[character]=frequency[character]+1
		else:
			frequency[character]=1   #{'a':1,'b':1}


	print(frequency)


main()	