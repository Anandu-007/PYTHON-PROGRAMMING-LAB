
# Dictionary and Set Operations

# 1. Create dictionaries
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"d": 40, "e": 50}

print("Dictionary 1:", d1)
print("Dictionary 2:", d2)

# 2. Merge dictionaries
merged = {**d1, **d2}
print("Merged dictionary:", merged)

# 3. Sort dictionary by keys
sorted_dict = dict(sorted(merged.items()))
print("Sorted dictionary:", sorted_dict)

# 4. Frequency counting
text = input("Enter a string: ")
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("Character frequency:", freq)

# 5. Create sets
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print("Set A:", a)
print("Set B:", b)

# 6. Union
print("Union:", a | b)

# 7. Common elements (intersection)
print("Common elements:", a & b)

# 8. Unique elements in A
print("Unique elements in A:", a - b)

# 9. Unique elements in B
print("Unique elements in B:", b - a)

# 10. Elements present in either set, but not both
print("Symmetric difference:", a ^ b)