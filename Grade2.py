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
		
		if (avg>=90):
		 grade='A+'
		 print("avg>=90")
		if (avg>=80 and avg <90):
		 grade ='A'
		 print("avg>=80")
		if (avg>=70 and avg <80):
		 grade ='B'
		 print("avg>=70")
		if (avg>=60 and avg <70):
		 grade ='C'
		 print("avg>=60")
		if (avg>=50 and avg <60):
		 grade ='D'
		 print("avg>=50")
		if(avg < 50):
		 grade='F'

		print("\Average Marks=:\t",avg)
		print("Grade:\t",grade) 


main()
