with open('txt file.txt') as file_object:
    file_contents = file_object.read() 

print(file_contents) 


with open(r'C:\Users\user\Downloads') as file_object_2: 
    file_contents_2 = file_object_2.read() 

print(file_contents_2)

file_name = r'C:\Users\user\Downloads'

with open (file_name, 'a') as file_object:
    file_object.write('Welcome to CS230!') 
   
   
 #lines = file_object.readlines()

 #for line in lines:
     #print(line)

#print(type(lines))



