books = []

def add_book():
    name = input("Enter book name: ")
    books.append(name)
    print("Book Added Successfully")

def view_books():
    print("\nBooks List:")
    for b in books:
        print(b)