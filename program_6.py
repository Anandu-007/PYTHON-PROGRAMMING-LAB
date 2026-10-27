
# List Operations

# Create a list
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Search for an element
x = int(input("Enter number to search: "))

if x in numbers:
    print("Element found")
else:
    print("Element not found")

# Update an element
numbers[1] = 25
print("After update:", numbers)

# Add an element
numbers.append(60)
print("After append:", numbers)

# Insert an element
numbers.insert(2, 35)
print("After insert:", numbers)

# Remove an element
numbers.remove(30)
print("After removal:", numbers)

# List comprehension: squares
squares = [n * n for n in numbers]
print("Squares:", squares)

# Filter even numbers
even = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even)

# Filter odd numbers
odd = [n for n in numbers if n % 2 != 0]
print("Odd numbers:", odd)

# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

# Pop an element
numbers.pop()
print("After pop:", numbers)

# Display length
print("Total elements:", len(numbers))