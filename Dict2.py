def main():


	#Write a program to create a dictionary namely Numerals 
	#from following two lists.
	#Keys = [‘One’, ‘Two’ , ’Three’]
	#Values= [1, 2, 3] 

	#{'One':1,'Two':2}...

	#a[0]=0

	#a[key]=value

	Keys = ['One', 'Two' , 'Three']
	Values= [1, 2, 3]

	key_val={}

	for i in range(0,len(Keys)):
	 	key_val[Keys[i]]=Values[i]


	print(key_val)



main()