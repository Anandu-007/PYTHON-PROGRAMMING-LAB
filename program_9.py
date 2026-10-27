def total(marks):
    return sum(marks)

def average(marks):
    return sum(marks) / len(marks)

def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")

    marks = []
    for j in range(3):
        mark = float(input("Enter mark: "))
        marks.append(mark)

    students.append((name, marks))

for name, marks in students:
    t = total(marks)
    avg = average(marks)

    print("\nName:", name)
    print("Total:", t)
    print("Average:", avg)
    print("Highest:", highest(marks))
    print("Lowest:", lowest(marks))
    print("Grade:", grade(avg))

students.sort(key=lambda x: total(x[1]), reverse=True)

print("\nStudents sorted by total marks:")

for name, marks in students:
    print(name, total(marks))