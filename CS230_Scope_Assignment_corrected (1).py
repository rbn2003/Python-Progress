
#Assignment Title: Understanding Python Scopes

#Instructions:

#1. Local Scope:
'''Write a Python function called 'local_scope_demo()' that demonstrates local scope. Inside this function, define a variable 'local_var' and print its value. 
Try to access 'local_var' outside the function and observe what happens.'''

#2. Enclosing (Non-local) Scope:
'''Create a function called 'enclosing_scope_demo()' that contains a nested function within it, named 'nested_function()'. Inside 'enclosing_scope_demo()', 
define a variable 'enclosing_var'. Attempt to modify the value of 'enclosing_var' from within 'nested_function()' and print its value outside both functions. 
Explain the output in your comments.'''

#3. Global Scope:
'''Declare a global variable 'global_var' outside any function. Write a function called 'global_scope_demo()' that prints the value of 'global_var'. 
Inside the function, try to modify the value of 'global_var' and print it again. Explain how the global variable behaves within functions.'''

#4. Built-in Scope:
'''Write a function called 'built_in_scope_demo()' that demonstrates the use of built-in functions in Python. Use at least three different built-in functions 
(for example, 'len()', 'max()', 'type()') within this function. Explain the purpose of each function and how they operate on different data types.'''

#### Submission Guidelines:
'''Write Python code for each of the tasks mentioned above. Include comments explaining each step and the expected output.
If there are any errors or unexpected outputs, try to explain the reason behind them. Submit the Python file with your code and explanations.'''



#Answer:1 

def local_scope_demo():
    local_var = "This is a Rabin Poudel" 
    print("Inside the function:", local_var)  #inside the function 

local_scope_demo()
print("Outside the function:", local_var)  #outside the function


#Answer:2

def enclosing_scope_demo():
    enclosing_var = "RONALDO is a GOAT"
    
    def nested_function():   #defining a nested function 
        nonlocal enclosing_var  
        enclosing_var = "Oh I am sorry, MESSI is a GOAT"
    
    nested_function()  #calling the nested function
    
    print("Value of enclosing_var after modification:", enclosing_var)   #this output demonstrates that the nested function has successfully modified the value of enclosing_var within its enclosing scope. 

enclosing_scope_demo() #calling the enclosing_scope_demo function.

#Answer:3 

  # Declaring a global variable outside any function

def global_scope_demo():
    global_var = "FIFA WORLDCUP 2014"
    global_var = "FIFA WORLDCUP 2022"     # Modifying the global variable
    print("Inside global_scope_demo(), global_var has been modified to:", global_var)

global_scope_demo() # Calling the function
 # Printing the value of the global variable after modification. 


#Answer:4 

def built_in_scope_demo():
    
    # Using len() to get the length of different data types
    
    string_length = len("Hello, Mr. Foster !")  # Returns the length of the string
    list_length = len([1, 2, 3, 4, 5])     # Returns the number of elements in the list
    dict_length = len({'a': 1, 'b': 2, 'c': 3})  # Returns the number of key-value pairs in the dictionary

    print("Length of 'Hello, Mr. Foster !':", string_length)
    print("Length of list:", list_length)
    print("Length of dictionary:", dict_length)

    # Using max() to find the maximum value in different data types

    max_of_list = max([1, 5, 3, 9, 2])  # Returns the maximum value in the list
    max_of_string = max("NIBAR")       # Returns the character with the maximum ASCII value in the string

    print("Max value in list:", max_of_list)
    print("Max character in 'NIBAR':", max_of_string)

    # Using type() to get the type of different objects
    type_of_integer = type(13)           # Returns the type 'int'
    type_of_string = type("KROOS")       # Returns the type 'str'
    type_of_list = type([1, 2, 3])       # Returns the type 'list'

    print("Type of integer:", type_of_integer)
    print("Type of string:", type_of_string)
    print("Type of list:", type_of_list)

# Calling the function to demonstrate
built_in_scope_demo()