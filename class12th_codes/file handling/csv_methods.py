import csv


myfile=open("mnc.csv",'a',newline="")

#write
# fw=csv.writer(myfile)

# print(type(fw))

# fw.writerow(['id','name'])
# fw.writerow(['1','Raj'])
# fw.writerow(['2','Moh'])

#read

# fr=csv.reader(myfile)

# print(type(fr))

# for i in fr:
# 	print(i)

#append

fw=csv.writer(myfile)

fw.writerow(['3','raju'])