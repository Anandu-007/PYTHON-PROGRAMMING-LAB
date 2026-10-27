def add_book():
    with open("books.txt", "a") as f:
        bid = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        f.write(bid + "," + title + "," + author + "\n")
    print("Book added successfully")

def search_book():
    key = input("Enter title or author to search: ")
    found = False

    try:
        with open("books.txt", "r") as f:
            for line in f:
                if key.lower() in line.lower():
                    print(line.strip())
                    found = True
    except FileNotFoundError:
        print("Catalogue not found")

    if not found:
        print("Book not found")

def report():
    try:
        with open("books.txt", "r") as f:
            books = f.readlines()

        print("Total books:", len(books))
        author = input("Enter author name: ")

        for book in books:
            if author.lower() in book.lower():
                print(book.strip())
    except FileNotFoundError:
        print("Catalogue not found")

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        report()
    elif choice == "4":
        break
    else:
        print("Invalid choice")