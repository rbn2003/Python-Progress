'''def my_first_function(customer, city): #function defination 
    """Display a welcome message"""
    print(f"Hello {customer.title()} from {city.title()}! How are you?") 

my_first_function('Rabin Poudel','Jacksonville') 
my_first_function('Jethalal','Gokuldham Society')''' 


def autos (color, year, make, model):
    """Display auto into!"""
    auto_1 = f"{color} {year} {make} {model}" 
    return auto_1
     

we_need_this_variable = autos('Red', '2024', 'Ford', 'Mustang')
print(we_need_this_variable) 

def get_employee_info (first_name, last_name, middle_name=''):
    """return employee full name""" 
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}" 

    return full_name.title()

print(get_employee_info('Rabin','Poudel', 'Sharma')) 
print(get_employee_info(last_name='Rabin', first_name='Poudel', middle_name='Sharma')) 

