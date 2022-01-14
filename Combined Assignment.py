#                           ANSWER 1

# this is a program to calculate the average of three numbers entered by the user

print("\n")
print("\n")
print("WELCOME")
num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))
num_3 = int(input("Enter third number:"))
avg = float((num_1 + num_2 + num_3)/3)
print("The average of the entered three number is " + str(avg))

print("\n")
print("\n")

#                           ANSWER 2

# this is a program to calculate the income tax of a person
# all units are in dollars
# people having a income less that 30000$ have to pay 0 tax

print("Let's calculate your income tax \nif u have income less than 30000 u will not have to pay any tax")
print("")
# gross income
gross_income = float(input("What is your income : "))
# deductions
standard_deduction = 10000
dependents_deduction = 3000
print("You will have a standard deduction of 10000$")
# dependents
no_of_dependents = int(input("How many dependent do u have :"))
print("You will have a deduction of 3000$ per dependent ")
if gross_income <= 30000:
    taxable_income = 0
else:
    taxable_income = gross_income - standard_deduction - (dependents_deduction*no_of_dependents)
print("Your taxable income is " + str(taxable_income)+"$")
rate = 20
tax = taxable_income*(rate/100)
print("Hence u will have to pay " + str(tax) + "$ as tax")

print("\n")
print("\n")

#                           ANSWER 3

# students =[SID, name, gender, course_name,CGPA]

print("Enter the following values to obtain a list")

name = input("Enter your name: ")  
SID = int(input("Enter your SID: "))
gender = input("Enter your gender ('M' 'F' 'U'): ")
course_name = input("Enter your course name: ")
CGPA = float(input("Enter your CGPA: "))
 
student = [SID, name, gender, course_name, CGPA]
print(student)

print("\n")
print("\n")

#                           ANSWER 4

# sorting of lists

marks1 = int(input("Enter marks of 1st student :"))
marks2 = int(input("Enter marks of 2nd student :"))
marks3 = int(input("Enter marks of 3rd student :"))
marks4 = int(input("Enter marks of 4th student :"))
marks5 = int(input("Enter marks of 5th student :"))

marks = [marks1, marks2, marks3, marks4, marks5]
print("normal list " + str(marks))

marks.sort()
print("sorted list " + str(marks))

print("\n")
print("\n")

#                           ANSWER 5

colour = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

print("normal output =" + str(colour))
colour.remove("Black")
print("output of part a =", colour)

colour = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
colour[3] = colour[4] = "Purple"
print("output of part b =", colour)

print("\n")
print("\n")

#                           THANK YOU
