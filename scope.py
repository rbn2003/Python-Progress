x = 20 #global 


#local scope
def my_function():
    x = 10 #local 
    print(x)
    print(x) 
print(x) 
my_function()        # ----->>> This would throw an error print(x) 
print(x) 

#enclosing scope
def outer_function(): 
    x = 10 #enclosing variable
    def inner_function():
        print(x)

    inner_function()

outer_function()

def power_function_factory(exponent):
    def power(x):
        return x**exponent
    return power 


square = power_function_factory(2)
cube = power_function_factory(3)
print(square(4))
print(cube(3)) 





