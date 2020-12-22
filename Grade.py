def main():
		sub1=float(input("Enter marks in subject1:\t"))
		sub2=float(input("Enter marks in subject2:\t"))
		sub3=float(input("Enter marks in subject3:\t"))
		sub4=float(input("Enter marks in subject4:\t"))
		sub5=float(input("Enter marks in subject5:\t"))
		total=sub1+sub2+sub3+sub4+sub5
		avg=total/5
		if avg<0 or avg>100:
		 grade=None
		
		if avg>=90:
		 grade='A+'
		 print("avg>=90")
		elif avg>=80:
		 grade ='A'
		 print("avg>=80")
		elif avg>=70:
		 grade ='B'
		 print("avg>=70")
		elif avg>=60:
		 grade ='C'
		 print("avg>=60")
		elif avg>=50:
		 grade ='D'
		 print("avg>=50")
		else:
		 grade='F'

		print("\Average Marks=:\t",avg)
		print("Grade:\t",grade) 


main()