'''

Your task is to prompt the user for a lower_bound value, and an upper_bound value. 
You must validate the input. The lower_bound value must be greater than 1, and the upper_bound must not be less than the lower_bound number. 
Once the input has been validated, print the lower_bound and upper_bound to the console. 
You will generate a range of integers between the lower_bound and upper_bound number. 
You will then check to see if a number in the range is prime or not. 
You will print f"{number} is prime!" and f"{{number} is not prime!} 


Some Tips:

lower_bound = input("lower_bound: ")

You might consider using a boolean flag. For example:

active = True
while active:
    lower_bound = input("lower_bound: ")
    if lower_bound <= 1:
        continue
    else:
        active = False

You can brute-force the primes. Remeber '%'?
You can use the % = modulus operator to find whether a number is prime. 

Example: 

if some_number % 2 == 0: 
    THAT NUMBER WOULD NOT BE PRIME!
'''

#YOUR CODE GOES HERE

##lower_bound = "Please enter a number for lower bound !"
##print (lower_bound)

##upper_bound = "Please enter a number for upper bound !"
##print (upper_bound)

active = True
while active:
    lower_bound = int (input("lower_bound: "))
    if lower_bound <= 1:
        continue
    else:
        active = False

   
active = True
while active:
    upper_bound = int(input("upper_bound: "))
    if upper_bound < lower_bound:
        continue
    else: 
        active = False 

print (f"the lower bound is:{lower_bound}" '\n'  f"the upper bound is: {upper_bound}")

for number in range (lower_bound, upper_bound+1):
   for m in range(2, number):
        if number % m == 0:
            print(f"{number} is not a prime number!")
            break
        else:
            print(f"{number} is a prime number!")
            break

    


