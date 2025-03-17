# prompts the user for their age
# Author: Sun Haoxiang
# Using read
age = int(input("enter your age: "))
if age <= 19:
    print("You are eligible for the student discount")
elif 20 <= age <= 54:
    print("you don't qualify for any age-related discounts")
else:
    print("You are eligible for the older discount")
