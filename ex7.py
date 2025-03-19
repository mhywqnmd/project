# Create the list of student names
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

# Print each name with the last name "Evans"
for name in studentNames:
    print(f"{name} Evans")

# Ask the user to add a new name
new_name = input("Please add another name to the list: ")

# Add the new name to the list
studentNames.append(new_name)

# Reprint the list with the last names
for name in studentNames:
    print(f"{name} Evans")
    
