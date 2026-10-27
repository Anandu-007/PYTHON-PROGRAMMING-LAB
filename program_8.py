s = input("Enter comma-separated numbers: ")

lst = s.split(",")
tup = tuple(lst)

print("List:", lst)
print("Tuple:", tup)

print("Total elements:", len(lst))
print("First element:", lst[0])
print("Last element:", lst[-1])

lst.reverse()
print("Reverse list:", lst)