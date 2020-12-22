def main():
	#print("String")
	# a="abc"
	# b="def"

	# c=a+b
	# print(c) #abcdef

	# print(a*3) #abcabcabc

	# print(a in c) #true

	# print(a not in c) #false

	# print(a==b)


	# a=43556

	# b=str(a)

	# if '0' in b:
	# 	print("0 present")

	# else:
	# 	print("0 not present")

	#a="abcdefg"

	# print(a[:])
	# print(a[::])

	# print(a[1:])
	# print(a[:2])

	# print(a[-3:])

	# print(a[1:2])

	#print(a[1::2])

	# print(a[::-1])

	
	#abc="abcdefabc12"

	# print(len(abc))


	# print(abc.capitalize())


	# print(abc.count("abc"))

	# print(abc.count("abc",1))


	# name="my name is"
	# n=len(name)

	# word=""
	# mod_string=""
	# for i in range(0,n):
	# 	if name[i]==" ":
	# 		print(word)
	# 		mod_string+=word.capitalize()+" "
	# 		word=""
	# 	else:
	# 		word+=name[i]
		
	# print(word) #is

	# mod_string+=word.capitalize()

	# print(mod_string) #My Name Is


	a="mathematics"
	n=len(a)
	b=""
	for i in range(0,n):
		if (i%2!=0):
			b+=a[i].upper()
		else:
			b+=a[i]

	print(b)
			





main()