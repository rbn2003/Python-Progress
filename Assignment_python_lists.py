#for question no1 
'''usernames = ['admin', 'nibar', 'subash', 'rabin', 'prajwol', 'aashish', 'sangee', 'kushal', 'sushant']

for username in usernames:
    if username == 'admin': 
        response = input(f"Welcome {username}! Do you need to view a status report? (yes/no): ")
        if response.lower() == 'yes':
            print("Here is the status report...")

        else:
            print("Okay, no problem.")
    else:
        print(f"Thanks for logging in, {username}!") 

#for question no2 
input_username = input("Enter your username: ")

if input_username in usernames:
    print("Welcome, Thanks for logging in!")
else:
    print("Sorry, We are unable to find you!") '''

#for question no3
current_usernames = ['Nibar2003', 'rabin2060', 'Viratkohli', 'LeoMessi10', 'CR7', 'Modric19', 'Kane2020', 'opera99', 'DHONI7', 'Kl01']
new_usernames = ['nibar2003', 'Rabin2060', 'viratkohli', 'leoMessi10', 'user5', 'user6', 'user7', 'user8']

for username in new_usernames:
    if username.lower() in [u.lower() for u in current_usernames]:
        print(f"The username '{username}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{username}' is available.") 

#for question 4 
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        ordinal = "1st"
    elif number == 2:
        ordinal = "2nd"
    elif number == 3:
        ordinal = "3rd"
    else:
        ordinal = str(number) + "th"
        
    print(ordinal)

