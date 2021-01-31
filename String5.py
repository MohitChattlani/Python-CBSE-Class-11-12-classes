def main():
	# STR = 'I enjoy working hello working in Python'

	# ABC= STR.partition("working")

	# print(ABC)
	#Uppercase(3),lowercase(6),alphabet(9),digit(3),symbol(2)
	string1="abc def 787 ABC &!"
	ucount=0
	lcount=0
	acount=0
	dccount=0
	scount=0

	n=len(string1)

	for i in range(0,n):
		letter=string1[i]
		if (letter.isupper()):
			ucount=ucount+1
		if (letter.islower()):
			lcount=lcount+1
		if (letter.isalpha()):
			acount=acount+1
		if (letter.isdigit()):
			dccount=dccount+1
		if (not(letter.isalnum()) and letter!=" "):
			scount=scount+1

	print("Upper:",ucount)
	print("Lower:",lcount)
	print("alphabet:",acount)
	print("Digit:",dccount)
	print("symbol:",scount)



main()