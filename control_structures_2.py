#simple if statements

'''age = 10

if age >= 21:
    print(f"You are {age} and old enough to buy an alcohol !")

else:
    print(f"You are {age} and not old enough to buy an alcohol !")'''

'''prompt = int(input("please enter your age: "))
print(prompt)

age = prompt 
if age < 5: 
    print(f"Price is $0.00")

elif age < 18:
    print(f"Price is $15.00")

else: 
    print(f"Price is $20.00")'''


'''requested_flavours = ['grape', 'strawberry', 'orange', 'banana']

if 'grape' in requested_flavours:
    print(f"Add grape to drink.")
if 'strawberry' in requested_flavours:
    print(f"Add strawberry to drink.")
if 'orange' in requested_flavours:
    print(f"Add orange to drink.")'''

#for loops

#my_colors = ['red', 'blue', 'green', 'yellow']


'''for color in my_colors:
    print(f"The color is: {color}")

for number in range(1,5):  
    print(number)

for number in range(1,20,5): #third number is for gap. 
    print(number)

my_string = "This is a string!"

for character in my_string:
    print(character)'''

#for loops with transfer statements 

'''my_colors = ['red', 'blue', 'green', 'yellow']
my_cars = ['ford', 'chevy', 'toyota', 'kia'] 

for color in my_colors:
    for car in my_cars:
        print(color, car)'''

'''for color in my_colors:
    if color == 'blue':
        break
    print(color)
else:
    print("That's all of the colors!")'''

'''my_num = 1                                     #initals counting 
while my_num <=20:                             #ending counting 
    print(my_num)
    my_num += 1

prompt = (f"Please enter a phrase, and I will repeat it: ")
prompt += "\nEnter 'quit to exit!" 

active = True 
while active: 
    message = input(prompt)
    if message.lower() == 'quit':
        active = False 
    else:
        print(message) '''

'''message = " "
while message != "quit":
    message = input (prompt)
    print(message)'''

'''while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)'''

my_num = 0
while my_num < 50:
    my_num += 1
    if my_num %2 == 0:
        continue

    print(my_num)
else:
    print("we are done talking about loops!")

my_range = range (2,100,2)
print(my_range)