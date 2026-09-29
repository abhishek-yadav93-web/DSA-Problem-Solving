def my_decorator(func):
    def second_func():
        print('hey')
        func()
        
    def wraper():
        print('hello')
        func()
        print('bye')
    return second_func # in there those function return that function executed the name() function 

@my_decorator # that line generally say name=my_decorator(name) name is the function pass in the deocrator function and 
def name():
    print('abhishek')

name() # that line generally say execute name function but inside there  name=decorator_funct()
print(name) 