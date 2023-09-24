

# factorial of a number 

# =============================================================================
# def factorial(n):
#     product=1
#     for i in range(1,n+1):
#         product=product*i
#     return product
# 
# 
# n=int(input('Enter the positive number: '))
# if n<0:
#     print('Factorial is not defined on negative number')
# else:
#     # factorial(n)
#     print('Factorial of ', n, 'is ',factorial(n))
# =============================================================================

# Fibonnacci Sequence:
# =============================================================================
#     0th fib bo = 0
#     1st fib bo = 1
#----------------------------------------------   
#     2nd fib no = 1
#     3rd fib no = 2
#     4th fib no = 3
#     5th fib no = 5
#     ......
#     ......
#     ......
#     nth fib no = fib(n-1)+fib(n-2)
#     
# =============================================================================

def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input('Enter the a non-negative number: '))
if n<0:
    print('Fibonacci numbers are Undefined for negative numbers')
else:
    print('Fibonnaci numbers at position ', n ,' is ', fibonacci(n))