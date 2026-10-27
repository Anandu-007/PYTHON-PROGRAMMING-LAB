# String Processing Operations
s = input("Enter a string: ")
# 1. Character replacement
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", s.replace(old, new))

# 2. String reversal
print("Reversed string:", s[::-1])

# 3. Palindrome checking
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 4. Character frequency
print("Character frequency:")
for ch in s:
    if s.index(ch) == s.index(ch):
        print(ch, ":", s.count(ch))
        
# 5. Word frequency
words = s.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word frequency:", freq)