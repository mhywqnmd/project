# takes in a number and returns the factorial of that number(for)
# Author: Sun Haoxiang
# Using read
def factorial_for(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# example
print(f"5! is: {factorial_for(5)}")
