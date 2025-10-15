# Input and Output
# Taking input
# Python's input() function is used to take user input.
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

# Printing Output
# At its core, printing output in Python is straightforward by to the print() function.
print("Hello, World!")

# Printing Variables
# Single variable
s = "Bob"
print(s)

# Multiple Variables
s = "Alice"
age = 25
city = "New York"
print(s, age, city)

# Take Multiple Input
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

# Str input
# Taking input as string
# color = str(input("What color is rose?: "))
color = input("What color is rose?: ") 
print(color)

# int input
# Taking input as int
n = int(input("How many roses?: "))
print(n)

# Float input
# Taking input as float
price = float(input("Price of each rose?: "))
print(price)
