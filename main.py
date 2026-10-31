from library import Library

def menu():
    print("\n===== SMART LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add book")
    print("2. Remove book")
    print("3. Search book")
    print("4. Display all books")
    print("5. Issue book")
    print("6. Return book")
    print("7. Reserve book")
    print("8. Process reservation")
    print("9. Sort books by title")
    print("0. Exit")
    return input("Choose an option: ").strip()

def main():
    library = Library()
    while True:
        choice = menu()
        if choice == "1":
            book_id = input("Book ID: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            library.add_book(book_id, title, author)
        elif choice == "2":
            library.remove_book(input("Book ID to remove: ").strip())
        elif choice == "3":
            query = input("Enter book ID or title: ").strip()
            book = library.search_book(query)
            print(book if book else "Book not found.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            library.issue_book(input("Book ID to issue: ").strip(),
                              input("Student name: ").strip())
        elif choice == "6":
            library.return_book(input("Book ID to return: ").strip())
        elif choice == "7":
            library.reserve_book(input("Book ID to reserve: ").strip(),
                                input("Student name: ").strip())
        elif choice == "8":
            library.process_reservation(input("Book ID: ").strip())
        elif choice == "9":
            library.display_sorted_books()
        elif choice == "0":
            print("Thank you for using the Smart Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
