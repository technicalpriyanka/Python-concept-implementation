#recursion in python
# recursion is a process in which a function calls itself as a subroutine. This means that the function will continue to call itself and repeat its behavior until some condition is met to return a result.

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))
print(factorial(5))
print(factorial(6))

#6 * factorial(5)
#6 * 5 * factorial(4)
#6 * 5 * 4 * factorial(3)   
#6 * 5 * 4 * 3 * factorial(2)
#6 * 5 * 4 * 3 * 2 * factorial(1)   #if condition is met, return 1
#6 * 5 * 4 * 3 * 2 * 1 = 720

#fibionacci series
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(7)) #output: 0
print(fibonacci(8)) #output: 1