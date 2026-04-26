# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("math :"))
english = int(input("english :"))
science = int(input("science :"))
tamil = int(input("tamil : "))

# Lets claculate the percentage of marks
sum = math+english+science+tamil
print("sum of math,english,science and tamil = ",sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)