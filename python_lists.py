
#systematic arrangement of things is called python lists 
'''x = 10
y = 20
z = x+y'''
 

#colors = ['red', 'blue', 'green', 'yellow']
#print(type(colors))
'''print(colors[2]) 
print(colors[3])
print(colors[-1])
print(colors[0]) 

#original lists
print(colors)

#dynamically modify the lists 
colors[2] = 'purple' 
print(colors) 
 
#modified lists
print(colors) 

colors.append('orange')
print(colors)'''

'''my_empty_lists = []
print(my_empty_lists)

my_empty_lists.append('red')
my_empty_lists.append('blue')
my_empty_lists.append('green')
my_empty_lists.append('orange')
print(my_empty_lists)

my_empty_lists.insert(2,'yellow')
print(my_empty_lists) 

del my_empty_lists[1]
print(my_empty_lists)''' 

'''new_list = [1,2,3,4,5,6,7,8,9,0]
print(new_list) 

popped_list_item = new_list.pop() 
print(new_list) 
print(popped_list_item) 

another_popped_item = new_list.pop(1) #(2) is removed in answer
print(new_list) 

new_list.remove(4)
print(new_list)''' 

list_of_words = ['zebra', 'apple', 'man', 'library', 'bear']
print(sorted(list_of_words))
print(list_of_words)
list_of_words.sort()
print(list_of_words) 


list_of_words.reverse()
print(list_of_words) 
list_of_words.reverse()
print(list_of_words) 

print(len(list_of_words)) 

list_of_colors = ['red', 'blue', 'yellow', 'black']
for color in list_of_colors:
    print(color)
    print("There are 5 colors in the list")

my_nums = list (range(1,11))
print(type(my_nums))
for i in my_nums:
    print(i) 

print(my_nums[0:4])

for num in my_nums[0:4]:
    print(f"The num is {num}")

my_nums_2 = my_nums[:]
print(my_nums_2)

print(my_nums)
print(*my_nums)
print(":::". join(str(my_nums)))

colors = (",". join(str(a) for a in list_of_colors))
print(colors) 

for num in list_of_colors:
    print(num, end=",")


