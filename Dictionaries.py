employee_info = {
                     'last_name': 'Poudel',
                     'first_name': 'Rabin',
                     'Address': '388 Quill Avenue',
                     'City': 'Jacksonville',
                     'State': 'Alabama',
                     'Zip': 36265,
                }

'''print(employee_info['Address'])
print(f"{employee_info['first_name']} {employee_info['last_name']}")  #printing 

employee_info['school'] = 'JSU'  #adding the list
print(employee_info) 

employee_info['City'] = 'Pokhara'  #modifiying the list
print(employee_info) 

print(employee_info['Zip'])
print(employee_info['Zipp']) #Incorrect keyvalue ZIPP'''


print(f"{employee_info.get('zipp', 'Key does not exist')}") 

for key, value in employee_info.items(): #printing both items 
    print(key)
    print(value)

for key in employee_info.keys():            
    print(key)

for value in employee_info.values():
    print(value)

outer_dictionary = {

             'employee_info': {'last_name': ['Poudel', 'Bell'], 'first_name': ['Rabin', 'Ben']}, 
                }

for key, value in outer_dictionary.items():
    for item in value:
        
        print(item)