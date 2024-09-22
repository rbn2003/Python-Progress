#Assignment Part I, 50 Points
#Any deviation away from my instructions will result in a 0.


#1. Write a simple function that prints one welcome message “Welcome to CS230-04”  - a. Call The Function

#2. Write a function that accepts the name of a city in Alabama and its county - a. Your function should simply print the name of the city and which county it is located in. 
#b. Make the county parameter a default value. Call the function for at least 2 cities and a third city that is not in the default county (think key-word arguments to override the default value).

#3. Write a function called movie_actors() that builds a dictionary describing a movie and the main star in that movie. Therefore, the function should take a movie name, 
#and an actor/actress name, and return a dictionary containing these two pieces of information. Use this function for three movies and their respective actor/actress 
#star. Print each one separately. 

#4. Make a list that contains 5 short bot texts. For example, your list could be: ‘hello’, ‘i am fine!’, ‘how are you?’, ‘it’s cold outside’, ‘it’s nice out today!’
#a. Pass the list to a function that prints each message. 
#b. Start with the above exercise and write a function called sent_messages() that prints the messages, but also moves each message to a new list called sent_messages as they are printed. 
# After calling the function, print both lists to make sure everything prints and moves accordingly. You can refer to the very last slide of the function pp presentation in canvas to complete this exercise.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Assignment Part II, 50 Points
#Any deviation away from my instructions will result in a 0.
#Import the random module

import random

#create a dictionary called new_users inside a function. Name your function " def my_dictionary_function(). You need to return the dictionary. 

#This dictionary will contain no values, only keys - so for every value, you will want to code an empty string. For example: {'key': ''}

#Your dictionary should contain 6 main keys ('user_id': 'credentials:' 'full_name': 'date_of_birth': 'address': and 'phone':)


#The FIRST key "user_id" is like any other key value pair, so list the key and the empty string '' as the value. 
#The keys "IN ORDER" (credentials, full_name, date_of_birth, address, and phone will all contain other dictionaires as values). For example: {'key': {'key': 'value', 'key': 'value'}}
#'credentials': dictionary keys are username and password (both with empty strings as values)
#'full_name': dictionary keys are first_name, middle_initial, last_name (all with empty strings as values)
#'date_of_birth: dictionary keys are birth_month, birth_day, birth_year (all with empty strings as values)
#'address': dictionary keys are street_name, city, state, zip (all with empty strings as values)
#'phone': dictionary keys are area_code, ph_number (both with empty strings as values)

#The above instructions might look like the following structure. You will replace "key" with the appropriate key:

#Function Declaration - USE THE FOLLOWING DICTIONARY STRUCTURE. Your first key is user_id with the empty string as the value. 
'''new_users = {  
                'user_id': '', 
                'key': {'key': '', 'key': '' },
                'key': {'key': '', 'key': '', 'key': '',}, 
                'key': {'key': '', 'key': '', 'key': '',},
                'key': {'key': '', 'key': '', 'key': '', 'key': '',},
                'key': {'key': '', 'key': ''},
                    
            }'''
#Return Statement RETURN THE DICTIONARY HERE. 

#After creating your dictionary function, Define a parameterized funtion called "get_user_info", you can simply use 'users' as your parameter. 

#Inside your new function:

#2. Inside the `get_user_info` function:
   
#3. Print a message to prompt the user to create a new user account.

#4. Generate a random 10-digit number (user_id) between 1000000000 and 9999999999.

#5. Convert the generated random number to a string and assign it to the 'user_id' key in the `users` dictionary.

#6. Iterate through each key-value pair in the `users` dictionary using a loop.

#7. For each key in the dictionary:
        #Check if the key is not equal to 'user_id'.
        #If it's not 'user_id', print the key as a category (e.g., 'credentials', 'full_name').

#8. For each subkey within the current category:
        #Prompt the user for input related to that subkey (e.g., if the category is 'credentials', prompt for 'username' and 'password').

#9. Update the corresponding subkey in the `users` dictionary with the user's input.

#10. Repeat steps 9-11 for each key and subkey combination in the dictionary.

#11. After collecting all user information, return the `users` dictionary from the `get_info()` function.

#12. Call the my_dictionary_function()

#13. Store the returned dictionary in a variable, such as `new_users`.

#14. Call the get_user_info() function passing as an argument your "new_users" dictionary reference

#15. print(new_user)



'''My answer begin from here:''' 

#My code begins here for Part I 

#1: Function to define welcome message 
def Welcome_Message():
    print("Welcome to CS230") 

#1(a): Calling the function 
Welcome_Message()

# 2. Function to print city and county in Alabama
def city_county(city, county="Default county"):
    print(f"The city of {city} is located in {county} County.") 

# 2(b) Call the function for at least 2 cities
city_county("Birmingham", "Jefferson")
city_county("Montgomery") 

# 2(b) Call the function for a city not in the default county using keyword arguments
city_county("SAMSUNG", county="Seoul") 

# 3. Function to build a dictionary describing a movie and its main star
def movie_actors(movie, actor):
    return {"Movie": movie, "Main Star": actor} 

# Use the function for three movies and actors
movie1 = movie_actors("Oppenheimer", "Cillian Murphy")
movie2 = movie_actors("The Wolf of Wall Street", "Leonardo DiCaprio")
movie3 = movie_actors("12th Fail", "Vikrant Massey")

print(movie1)
print(movie2)
print(movie3)

# 4a. List of short bot texts
bot_texts = ['Hi', 'I am at Alabama!', 'Where are you?', 'Its cold here.', 'Its nice today!']

# Function to print each message
def print_messages(messages):
    for message in messages:
        print(message)

# Call the function to print each message
print_messages(bot_texts) 

# 4b. Function to print messages and move them to a new list
def sent_messages(messages):
    sent_messages = []
    for message in messages:
        print(message)
        sent_messages.append(message)
    return sent_messages

# Call the function and print both lists
sent = sent_messages(bot_texts)
print("Original list:", bot_texts)
print("Sent messages list:", sent)

#My code begins here for Part II 


import random

# Create a dictionary function
def my_dictionary_function():
    new_users = {
        'user_id': '', 
        'credentials': {'username': '', 'password': ''},
        'full_name': {'first_name': '', 'middle_initial': '', 'last_name': ''}, 
        'date_of_birth': {'birth_month': '', 'birth_day': '', 'birth_year': ''},
        'address': {'street_name': '', 'city': '', 'state': '', 'zip': ''},
        'phone': {'area_code': '', 'ph_number': ''},
    }
    return new_users

# Define a function to get user info
def get_user_info(users):
    print("Please create a new user account.")
    users['user_id'] = str(random.randint(1000000000, 9999999999))
    for key, value in users.items():
        if key != 'user_id':
            print(f"Enter your {key}:")
            for subkey in value:
                value[subkey] = input(f"{subkey.title()}: ")
    return users

#Call the my_dictionary_function and get_user_info
new_users = my_dictionary_function()
new_user = get_user_info(new_users)

#Print the new user dictionary
print(new_user)




 