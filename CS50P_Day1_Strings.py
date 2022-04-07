# The first default program
print("Hello, World")

# Asking for input in variable "name"
name = input("What is your name? ")

# Splice the string uisng method
name = name.strip()

# Capitalize the first letter of each Name
name = name.title()

# Output Say hello to the user
print("Using argument:")
print("Hello,", name)

# Output 2
print("Using Concatenation:")
print("Hello, " + name)

# Output 3
print("Using formatted string")
print(f'Hello, {name}')

# Output 4 Changing end to nothing or space to nothing
print("Changing Default Argument or parameter:")
print("Hello, ", end="")
print(name)


# Ask again for clean coding
name = input("Sorry, what is your name again ? ").strip().title()
print("Hello, ", name)
