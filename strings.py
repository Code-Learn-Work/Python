string1 = 'Hello'
string2 = "Hello"
string3 = """Hello"""
print(string1 + " == " + string2 + " == " + string3)
print("hello".capitalize())
print("hello".replace("e","a"))
print("hello".isalpha())
print("123".isdigit())

# Some other useful functions in Python 
# 1. split()
# 2. format()

print("some,csv,values".split(","))

name = "Mayank"
machine = "JARVIS"

print("Nice to meet you {0}. I am {1}".format(name,machine))
 
# Similar to this 
print(f"Nice to meet you {name}. I am {machine}")