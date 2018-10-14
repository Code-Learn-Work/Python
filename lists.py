student_names = []

# List already having data

student_names = ["Mark", "Jessica", "Katrina"]

# For accessing values we use index

print(student_names[0]) # Mark
print(student_names[2]) # Katrina

print(student_names[-1]) # Katrina

student_names[0] = "James" # Replace the first element of the list
print(student_names)

student_names.append("Homes") # Add at the end
print(student_names)

print("Katrina" in student_names)

print(len(student_names))

student_names[1] = None
print(student_names)

del student_names[1]
print(student_names)

# List Slicing

print(student_names[1:]) # ["Katrina","Homes"]
print(student_names[1:-1])