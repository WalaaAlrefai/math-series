# Function for nth Fibonacci number
def fibonacci(n):
    '''
    This function calculate the Fibonacci for integer
    parameter n : int,
    return int
    '''
   
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
    '''
    This function calculate the Lucas for integer
    parameter n : int,
    return int
    '''

    if n < 0:
        return("Incorrect input")
   
    # Base cases
    if n == 0:
        return 2
    if n == 1:
        return 1
   
    # recurrence relation
    return lucas(n - 1) + lucas(n - 2)
     
def sum_series(n,a=0,b=1):
     '''
    This function calculate the sumation series for integer
    parameter n / a / b : int,
    return int
    '''
     
     if n == 0:
        return a
     elif n == 1:
        return b
     else:
        return sum_series(n-1, a, b)+sum_series(n-2, a, b)
     
    #  if x == 0 and y == 1:
    #     return fibonacci(n-1) + fibonacci(n-2)
    #  elif x == 2 and y == 1:
    #     return lucas(n - 1) + lucas(n - 2)
    #  else:
    #      return sum_series(n-1, x, y)+sum_series(n-2, x, y)
        #  while (n != 0):
        #    return( sum(n - 1) + sum(n - 2))

# Driver code to test above methods
n = 9
print(lucas(n))   
print(fibonacci(n))
print(sum_series(5,2,3))