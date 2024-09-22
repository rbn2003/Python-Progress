'''def users(first_name, last_name):
    """Return Full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True: 
    first_name = input("Enter first name or 'q' to quit: ")
    if first_name == 'q':
        break
    last_name = input("Enter last name or 'q' to quit: ")
    if last_name == 'q':
        break 

    user_1 = users(first_name, last_name)
    print(f"Welcome {user_1}")''' 

dictionary_1 = {

    'employee': {'last_name': 'Poudel', 'first_name': 'Nibar'},
    'employee_address': {'street': '388 Quill Avenue NW', 'city': 'Jacksonville'}, 
    'empls_fav_food': {'Pizza', 'Burger', 'Hotdogs', 'Cake'},
    }

for key, value in dictionary_1.items():
    if key == 'employee':
        for key_2, value_2 in dictionary_1.items():
            print(key_2, value_2)
    elif key == 'employee_address':
        for key_3, value_3 in value.items(): 
            print(key_3, value_3) 
    elif key == 'empls_fav_food':
        for item in value:
            print(*item)
