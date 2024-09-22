#Complete Steps 1-7 First

#1
'''1. Assign a message to a variable, and then print that message. Comment your code!
2. Assign a message to a variable, then assign a person's name to a variable called "name" - Print the message and the person's name! Comment your code!
3. Use a variable to represent a person's name, and then print it in lowercase, uppercase, and title case. Comment your code!
4. Use a famous movie quote or song line. Assign it to a variable. Assign the artist who is famous for the quote and assign it to a variable. Print the artist and the quote. Comment your code! 
5. Write some addition, subtraction, multiplication and division problems for the following numbers: (444+555), (456-897), (234*777), (1232345/345). For each problem, use a variable for 
each number in the problem. For example "333 + 444" would be "x = 333" "y = 444". Then add the variables together like x + y. However, you must remember that we need somewhere to store our 
solutions, so you might could initialize the variable "z" to 0. Therefore, z = x + y and so on. Comment your code!
6. Use a variable to represent your favorite number, then create a message that reveals your favorite number. Comment your code!
7. Code an example of each of the following built-in datatypes in python: int, float, string. Create a variable for each and then print each one to the console. 
'''
#Your code goes here:

message = "Hello Professor!"
print (message)

messageII = "United States of America"
name = "Rabin Poudel"
print (f"{messageII}, {name}")

person_name = "Rabin Poudel"
print(f"Lowercase: {person_name.lower()}")
print(f"Uppercase: {person_name.upper()}")
print(f"Titlecase: {person_name.title()}")

movie_quote ="Embrace all the sufferings for what is life without those little victories"
artist_name = "Nibar Poudel"
print (f"{movie_quote}- {artist_name}!")

num1_x = 444
num2_y = 555
z_add = num1_x + num2_y

num3_x = 456
num4_y = 897
z_sub = num3_x - num4_y

num5_x = 234
num6_y = 777
z_multilication = num5_x * num6_y

num7_x = 1232345
num8_y = 345
z_division = num7_x / num8_y

print(f"Addition: {z_add}")
print(f"Subtraction: {z_sub}")
print(f"Multiplication: {z_multilication}")
print(f"Division: {z_division}")

favourite_number = 18
print (f"My favourite number is : {favourite_number}" )

int_variable = 18
float_variable = 18.01
string_variable = "Hello JAX State" 

print(f"Integer: {int_variable}")
print(f"float: {float_variable}")
print(f"String: {string_variable}")


#------------------------------------------------------------------------------------------------------------------------------------
#2
'''
Create a Python program with the following requirements:
Declare three variables: var_1, var_2 and var_3.
Initialize each variable as follows:
var_1 with an integer value;
var_2 with a floating-point number;
var_3 with a string;
Print the type and value of each variable!
'''
#Your code goes here:

var_1 = 35 #integer
var_2 = 34.4 #floating_number
var_3 = "This is Pokhara"
print(f"var_1 - Type: {type(var_1)}, value: {var_1}")
print(f"var_2 - Type: {type(var_2)}, value: {var_2}")
print(f"var_3 - Type: {type(var_3)}, value: {var_3}") 



#------------------------------------------------------------------------------------------------------------------------------------
#3
'''
Implement dynamic variable changes:
Change the value of var_1 to a boolean;
Change the value of var_2 to a string;
Change the value of var_3 to a list containing at least three elements of different data types;
Print the type and value of each variable after the changes!
'''
#Your code goes here:

var_1 = 42  # Integer value
var_2 = 3.14  # Floating-point number
var_3 = "Jacksonville"  # String

print(f"Initial var_1 - Type: {type(var_1)}, Value: {var_1}")
print(f"Initial var_2 - Type: {type(var_2)}, Value: {var_2}")
print(f"Initial var_3 - Type: {type(var_3)}, Value: {var_3}")

var_1 = True

var_2 = "Updated String"

var_3 = [1, "two", 3.0]

print(f"Updated var_1 - Type: {type(var_1)}, Value: {var_1}")
print(f"Updated var_2 - Type: {type(var_2)}, Value: {var_2}")
print(f"Updated var_3 - Type: {type(var_3)}, Value: {var_3}")


#------------------------------------------------------------------------------------------------------------------------------------
#4
'''
Demonstrate implicit vs explicit type conversion:
Perform an operation on var_1 and var_2 (demonstrate implicit conversion)
Perform another operation on var_1 and var_2 (demonstrate explict conversion otherwise known as type casting!) 
Yes! You will need to initialize new variables for each example. 

'''
#Your code goes here:

var_1 = 42  # Integer value
var_2 = 3.14  # Floating-point number

result_implicit = var_1 + var_2
print(f"Implicit Conversion Result: {result_implicit}")

var_1_float = float(var_1)
result_explicit = var_1_float + var_2
print(f"Explicit Conversion Result: {result_explicit}")



#------------------------------------------------------------------------------------------------------------------------------------
#5
'''
The input function:

user_input = input("Please enter a name here: ")


Use the input function to take user input for each variable with initially string-typed values. 
Perform explicit type conversion for each variable to dynamically change their types (integer, float, string). 
Print the type and value of each variable after user input. 

'''
#Your code goes here:


user_input_str = input("Please enter a name here: ")

user_input_int = input("Please enter an integer: ")
user_input_int = int(user_input_int)  # Explicitly converting to integer

user_input_float = input("Please enter a floating-point number: ")
user_input_float = float(user_input_float)  # Explicitly converting to float

print("Type and value of user_input_str:", type(user_input_str), user_input_str)
print("Type and value of user_input_int:", type(user_input_int), user_input_int)
print("Type and value of user_input_float:", type(user_input_float), user_input_float)



#------------------------------------------------------------------------------------------------------------------------------------
#6
'''
BONUS!
Demonstrate String Manipulation:
Extract a substring from var_3 and store it in a new variable called my_substring_variable;
Concatenate my_substring_varaibale with the orignal value of var_3
Print the final value of var_3 after the concatenation. 

'''
#Your code goes here:


var_3 = "Hello, World!"

my_substring_variable = var_3[7:12]  # Extracting "World" as a substring

var_3 = var_3 + my_substring_variable

print("Final value of var_3 after concatenation:", var_3)

