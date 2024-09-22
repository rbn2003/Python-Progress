my_integer = 1234 

float_value = 123.45
print(float_value) 

the_string = "Hello, this is Nibar Poudel"
print(the_string) 

list_integer = [1,2,3,4,5,6,]
for num in list_integer: 
    print(num) 

the_dictionary = {
    "First_Name": "Nibar",
    "Last_Name": "Poudel",
    "Major": "Computer Science",
    "Country": "Nepal" 
}

count = 0
for key in the_dictionary.items():
    print(key)

print ("First_Name:", the_dictionary["First_Name"])
print ("Last_Name:", the_dictionary["Last_Name"])
print ("Major:", the_dictionary["Major"])
print ("Country:", the_dictionary["Country"]) 


my_integer = 1234                        #implicit way of doing this 
my_float = my_integer + 0.0
print(my_float) 

my_integer = 1234                        #explicit way of doing this 
the_float = float(my_integer)
print(the_float) 


first_integer = 1234                     #addition of integer and string 
first_string = "2345"
result = first_integer + int(first_string)
print(result)

def Greet(name):
    """This function greets the user with the given name."""
    print("Hello, " + name + "!") 
Greet("Nibar")  


def greet(first_name, last_name, greeting='Namaste'):         #name (str): The name of the person to greet.
                                                              #greeting (str, optional): The greeting to use. Defaults to Namaste.
    return f"{greeting}, {first_name}, {last_name}!" 
print(greet(fisrt_name='Nibar', last_name='Poudel')) 

