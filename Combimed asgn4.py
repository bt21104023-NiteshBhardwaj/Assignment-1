    #
   ##
  # #
    #
    #
    #
 #######   
# Answer 1
print("QUESTION 1")

def hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print(f"Move disk 1 from peg {source} to peg {target}")
        return
 
    hanoi(disks - 1, source, target, auxiliary)
    print(f"Move disk {disks} from peg {target} to peg {target}")
    hanoi(disks - 1, auxiliary, source, target)

 
disks = int(input("Enter number of disks: "))
hanoi(disks, "A", "B", "C")

print()
print()
###################################################################################################

    ##########
             #
             #
     ########
    #
    #
     #########
# Answer 2
print("QUESTION 2")

# input
rows = int(input("How many rows u want in pascals triangle : "))

# the master list contains the rows of pascal's triangle
master_list = list()

master_list.append([1])                                         # row one of the pascal's triangle

master_list.append([1, 1])                                      # row two of the pascal's triangle


# function for new row
def new_row():
    temp_list = master_list[len(master_list)-1]                 # temp list contains the previous row of pascal's triangle
    new_list = [1]                                              # first element of the next list is 1 
    
    for x in range(0, len(master_list)-1):
        new_list.append(temp_list[x] + temp_list[x+1]) 
    
    new_list.append(1)                                          # last element is also a one
    master_list.append(new_list)


for n in range(2, rows):                                        # adding rows to triangle
    new_row()

for item in master_list:                                        # displaying the list
    print(item, end="\n\n")

print()
print()
###################################################################################################

    #########
             #
             #
    #########
             #
             #
    #########

# Answer 3
print("QUESTION 3")

# user input
dividend = int(input("Enter dividend : "))
divisor = int(input("Enter divisor : "))

# quotient remainder
quotient = (dividend // divisor)
remainder = dividend % divisor
elements = [quotient, remainder]

if divisor == 0:
    print("Division not possible")
else:
    print(f"\nHence u have")
    print(f"Quotient : {quotient}")
    print(f"Remainder : {remainder}")
    print()
    print("a) Is quotient callable  : ", callable(quotient), "\nIs remainder callable  : ", callable(remainder), end="\n\n")
    print("b) Is all values are zero : ", (quotient, remainder) == (0, 0), end="\n\n")
    elements.append(4)
    elements.append(5)
    elements.append(6)
    print("c) Appending 4 5 6 in quotient and remainder : ", elements, end="\n\n")
    elements = set(elements)
    print("d) Converting into a set : ", elements, end="\n\n")
    elements = frozenset(elements)
    print("e) Making it immutable : ", elements, end="\n\n")
    print("f) Largest element of the set is ", max(elements), end="\n\n")

print()
print()
###################################################################################################

    #        #
    #        #
    #        #
    #        #
     #########
             #
             #
             #
             #

# Answer 4
print("QUESTION 4")

# Define class 
class Students:
    def __init__(self, name: str, roll_no: int):
        self.name = name
        self.roll_no = roll_no 

    def students_details(self):
        return f"The student name is {self.name} \nHis roll number is {self.roll_no}\n"
    
    def __del__(self):
        print("Student's record deleted ", self.name)


# Four objects
student_1 = Students("Jean", 10)
student_2 = Students("Eren", 5)
student_3 = Students("Levi", 3)
student_4 = Students("Armin", 8)
# Using methods
print("1) ", student_1.students_details())
print("2) ", student_2.students_details())
print("3) ", student_3.students_details())
print("4) ", student_4.students_details())
# Deleting 
del Students

print()
print()
###################################################################################################

    ##########
    #
    #
    #
     #########
             #
             #
             #
    #########

# Answer 5
print("QUESTION 5")

# Define class 
class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary 

    def employee_details(self):
        return (f"Employee : {self.name} \t Salary : {self.salary}\n")

# Four objects
employee_1 = Employee("Mehak", 40000)
employee_2 = Employee("Ashok", 50000)
employee_3 = Employee("Viren", 60000)
# Using methods
print("1) ", employee_1.employee_details())
print("2) ", employee_2.employee_details())
print("3) ", employee_3.employee_details())

# Deleting Viren record
del employee_3
# Changing attribute of an object
employee_1.salary = 70000

print("UPDATED RECORD\n")

print("1) ", employee_1.employee_details())
print("2) ", employee_2.employee_details())

print()
print()
###################################################################################################

    #
    #
    #
    #
    #########
    #        #
    #        #
    #########
# Answer 6
print("QUESTION 6")

# input from George and Barbie
word_1 = input("Word by Barbie : ")
word_2 = input("Word by George : ")
# making a set of the letters of their input
word_1 = set(word_1.lower())
word_2 = set(word_2.lower())

# print(word_1)
# print(word_2)

print("\n\n\n\n")
# logic
if word_1 == word_2 :
    print("Your friendship is true")
else:
    print("Your friendship is fake")

print()
print()
###################################################################################################

