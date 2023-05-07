# Function for nth Fibonacci number
def fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        return("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def lucas(n):

    if n < 0:
        return("Incorrect input")
   
    # Base cases
    if n == 0:
        return 2
    if n == 1:
        return 1
   
    # recurrence relation
    return lucas(n - 1) + lucas(n - 2)
     
def sum_series(n,x=0,y=1):
    if x == 0 and y == 1:
        return fibonacci(n-1) + fibonacci(n-2)
    elif x == 2 and y == 1:
        return lucas(n - 1) + lucas(n - 2)
    else:
        while (n != 0):
          return( sum(n - 1) + sum(n - 2))

# Driver code to test above methods
n = 9
print(lucas(n))   
print(fibonacci(n))
print(sum_series(5,2,3))