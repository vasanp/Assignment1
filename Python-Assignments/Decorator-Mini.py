def multiply_twice(func):
   def wrapper(num1, num2):
       
       call1 = func(num1,num2)
       call2 = func(num1,num2)
       
       return call1,call2
   return wrapper
    
@multiply_twice
def multiply(num1,num2):
    print(num1*num2)
     

multiply(5,6)

# Create a generator to return the fibonnaci sequence

def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a + b 

for x in fibo(12):
    print(x, end =" ")
