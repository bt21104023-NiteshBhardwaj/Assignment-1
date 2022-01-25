# **********Answer 1**************
print("\n")
print("\n")
# GIVEN
given_input_string = "Python is a case sensitive language"
# ANS TO ALL PARTS
print("a)", len(given_input_string))
print("b)", given_input_string[::-1])
part_c = given_input_string[10:26]
print("c)", part_c)
print("d)", given_input_string.replace("a case sensitive", "object oriented"))
print("e)", given_input_string.index("a"))
print("f)", given_input_string.replace(" ", ""))

print("\n")
print("\n")

# **********Answer 2**************

# VARIABLES
name = "Nitesh Bhardwaj"
SID = 21104023
department_name = "Electrical"
CGPA = 9.9
# STRING FORMATTING
print("Hey, {0} Here!".format(name))
print("My SID is {0}".format(SID))
print("I am from {0} department and my CGPA is {1}".format(department_name, CGPA))

print("\n")
print("\n")

# **********Answer 3**************
a = 56
b = 10
# ANS TO ALL PARTS
print("a) a&b : ", a & b)
print("b) a|b : ", a | b)
print("c) a^b : ", a ^ b)
print(f"d) left shift a with 2 bits : {a << 2} \t  left shift b with 2 bits : {b << 2}")
print(f"e) right shift a with 2 bits : {a >> 2} \t  right shift b with 4 bits : {b >> 4}")

print("\n")
print("\n")

# **********Answer 4**************
# INPUT
num_1 = float(input("Enter the first number:"))
num_2 = float(input("Enter the second number:"))
num_3 = float(input("Enter the third number:"))
# LOGIC
if num_2 < num_1 and num_3 < num_1:
    print("The greatest number is ", num_1)
elif num_3 < num_2 and num_1 < num_2:
    print("The greatest number is ", num_2)
elif num_1 < num_3 and num_2 < num_3:
    print("The greatest number is ", num_3)

print("\n")
print("\n")

# **********Answer 5**************
# INPUT
input_string = input("Please give input string : ")

# LOGIC
var = input_string.find("name")
if var >= 0:
    print("is \"name\" there in the string : \nyes")
else: 
    print("is \"name\" there in the string : \n5no")

print("\n")
print("\n")

# **********Answer 6**************
# INPUT
side_1 = input("Enter the length of side 1: ")
side_2 = input("Enter the length of side 2: ")
side_3 = input("Enter the length of side 3: ")
# CHANGING INPUT TO FLOAT TYPE
side_1 = float(side_1)
side_2 = float(side_2)
side_3 = float(side_3)
print("Can the triangle be formed ??")
# LOGIC
if side_1 + side_2 < side_3 or side_1 + side_3 < side_2 or side_2 + side_3 < side_1:
    print("No")
elif side_1 + side_2 == side_3 or side_1 + side_3 == side_2 or side_2 + side_3 == side_1:
    print("The given lengths are of  a line with a point in between ")
else:
    print("Yes")

print("\n")
print("\n")

# **********THANK YOU**************
