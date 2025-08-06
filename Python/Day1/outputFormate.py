amount = 150.75
print("Amount: ${:.3f}".format(amount))

# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")

# Seprating with Comma
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')

# Using f-string
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")


# : Using % Operato
# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" %add)