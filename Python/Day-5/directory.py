d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

d = { "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)

d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)


d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

    import copy
original = {'name': 'Alice', 'marks': {'math': 90, 'science': 95}}

# Create a shallow copy
shallow = copy.copy(original)

# Modify nested value in the copy
shallow['marks']['math'] = 100

print("Original:", original)
print("Shallow Copy:", shallow)



import copy
original = {'name': 'Alice', 'marks': {'math': 90, 'science': 95}}

# Create a deep copy
deep = copy.deepcopy(original)

# Modify nested value in the deep copy
deep['marks']['math'] = 100

print("Original:", original)
print("Deep Copy:", deep)