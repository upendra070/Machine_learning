s = {10, 50, 20}
print(s)
print(type(s))

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)


# Python program to demonstrate differences
# between normal and frozen set

# Same as {"a", "b","c"}
s = set(["a", "b","c"])

print("Normal Set")
print(s)

# A frozen set
fs = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(fs)

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# fs.add("h")``