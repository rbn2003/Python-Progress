#Here's how my code begins: 

#this is the code for question no. 1

customer = {  #Creating the dictionary. 
    'first_name': 'Rabin',
    'last_name': 'Poudel',
    'age': 19,
    'state': 'Gandaki',
    'city': 'Pokhara',
    'zip': '33700'
}

print("Customer Information: ")    #Printing of the dictionary details 
print(customer)
         
print("City:", customer['city'])     #printing city & state only 
print("State:", customer['state']) 

customer['annual_salary'] = 6000,  #adding new key-value 

print("\nCustomer information with annual salary:")    #printing after adding annual salary 
print(customer)

customer['zip'] = '33800'          #modifying zip code data 

print("\nCustomer information after modifying zip:")     #printing after modifying zip code 
print(customer)  

del customer['zip']     #deleting the zip from dictionary customer 

print("\nCustomer information after removing zip:")    #printing customer information after removing zip
print(customer)


#this is the code for question number 2 

courses = {                                   #creating a dictionary 
    'CS230' : 'Fundamentals of Computing', 
    'AN224' : 'Introduction to Anthropology',
    'MS112' : 'Precalculus Algebra',
    'THR242': 'Introduction to Theatre',
    'ENG101': 'English Composition'

}

print("Course names and their respective course numbers: ")    #printing the original dictionary for 5 courses 
print(courses) 

course_key = 'CS230'                                          #using the get() function to get the assigned course name with the course key value
print(course_key, ":", courses.get(course_key))  

non_existing_key = 'MS100'                                    #for non_existing key 
print(non_existing_key, ":", courses.get(non_existing_key, "Key Doesn't Exist")) 

for key in courses.keys():                                 #printing all keys 
    print(key) 

for value in courses.values():                             #printing all values 
    print(value)


#this is my code for the question number 3 

counties = {                                          #creating new dictionary. Thanks Mr.Foster, I got to know that here are 42 counties in total at Alabama because of this question, HAHA. 
    'Jefferson': 'Birmingham',
    'Montgomery': 'Montgomery',
    'Mobile': 'Mobile',
    'Madison': 'Huntsville' 
}

for county, city_center in counties.items():           #printing the county with their city center 
    print(f"{city_center} is the city center of {county}")

for city_center in counties.values():                  #printing the only city centers 
    print(city_center)


for county in counties.keys():                         #printing the only counties from the dictionary. 
    print(county)

#this is my code for the question number 4 

burger_order = {
    'size': 'Double',
    'cheese': 'YES',
    'toppings': ['Katsup', 'Mustard', 'Pickles', 'Onions', 'Lettuce', 'Tomato']
}

#using join statement, it joins the lower f string with the first f string. 

summary = f"Your {burger_order['size']} burger with cheese ({burger_order['cheese']}) and toppings: "\
          f"{', '.join([topping for topping in burger_order['toppings']])}."                 

print(summary)


#this is my code for question number 5 


book_1 = {
    'book_title': 'How I connect my life to my Planets',
    'author': 'Nibar Poudel',
    'publication_date': 'July 18, 2013',
    'number_of_pages': 213
}

book_2 = {
    'book_title': 'Bloodlands: Europe Between Hitler and Stalin',    #Mr.Foster I suggest you to read this book on your holidays. 
    'author': 'Timothy Snyder',
    'publication_date': ' December 29, 2010 ',
    'number_of_pages': 319
}

book_3 = {
    'book_title': 'Cult Classic Massey',
    'author': 'Nibar Poudel',
    'publication_date': 'December 29, 2003 ',
    'number_of_pages': 118
}
 
list_of_books = [book_1, book_2, book_3]

for book in list_of_books:
    print("Book Title:", book['book_title'])
    print("Author:", book['author'])
    print("Publication Date:", book['publication_date'])
    print("Number of Pages:", book['number_of_pages'])
    print()  

