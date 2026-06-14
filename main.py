from student import *
from book import *
from transaction import *

while True:
    print("\nLibrary Management System")
    print("1. Student Module")
    print("2. Book Module")
    print("3. Transaction Module")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Student Module Active")
    elif choice == "2":
        print("Book Module Active")
    elif choice == "3":
        print("Transaction Module Active")
    elif choice == "4":
        break
    else:
        print("Invalid Choice")
