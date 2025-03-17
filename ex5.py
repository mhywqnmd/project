# takes in a number and returns the factorial of that number(while)
# Author: Sun Haoxiang
# Using read
def factorial_while(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

# example
print(f"5! is: {factorial_while(5)}")
