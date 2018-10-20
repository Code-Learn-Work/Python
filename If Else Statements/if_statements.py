number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

if number:
    print("Number has a Truthy value")
else:
    print("Number has a Falsy value")

new_number=0

if new_number:
    print("This will not be printed")
else:
    print("New Number is not defined and Falsy")

python_course = True

if number == 5 and python_course:
    print("This will execute")

if number == 17 or python_course:
    print("This will also execute")

# Terenary operators in Python
a = 1
b = 2

print("Bigger" if a > b else "Smaller")