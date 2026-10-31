from collections import deque
from book import Book

class Node:
    """Node for the linked list of books."""
    def __init__(self, book):
        self.book = book
        self.next = None

class Library:
    def __init__(self):
        self.head = None
        self.books_by_id = {}          # Hash table: book ID -> Book
        self.reservations = {}         # Book ID -> FIFO queue of student names

    def add_book(self, book_id, title, author):
        if not book_id or not title or not author:
            print("Book ID, title, and author are required.")
            return
        if book_id in self.books_by_id:
            print("A book with that ID already exists.")
            return
        book = Book(book_id, title, author)
        node = Node(book)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.books_by_id[book_id] = book
        self.reservations[book_id] = deque()
        print("Book added successfully.")

    def remove_book(self, book_id):
        if book_id not in self.books_by_id:
            print("Book not found.")
            return
        if not self.books_by_id[book_id].available:
            print("Cannot remove an issued book.")
            return
        previous = None
        current = self.head
        while current:
            if current.book.book_id == book_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                del self.books_by_id[book_id]
                self.reservations.pop(book_id, None)
                print("Book removed successfully.")
                return
            previous, current = current, current.next

    def search_book(self, query):
        # Average O(1) by ID; O(n) title search through linked list.
        if query in self.books_by_id:
            return self.books_by_id[query]
        query_lower = query.lower()
        current = self.head
        while current:
            if query_lower in current.book.title.lower():
                return current.book
            current = current.next
        return None

    def display_books(self):
        if self.head is None:
            print("No books in the library.")
            return
        current = self.head
        while current:
            print(current.book)
            current = current.next

    def issue_book(self, book_id, student):
        book = self.books_by_id.get(book_id)
        if not book:
            print("Book not found.")
        elif not book.available:
            print("Book is already issued.")
        else:
            book.available = False
            book.issued_to = student
            print(f"'{book.title}' issued to {student}.")

    def return_book(self, book_id):
        book = self.books_by_id.get(book_id)
        if not book:
            print("Book not found.")
        elif book.available:
            print("This book is not currently issued.")
        else:
            book.available = True
            book.issued_to = None
            print(f"'{book.title}' returned successfully.")
            if self.reservations[book_id]:
                next_student = self.reservations[book_id][0]
                print(f"Reservation queue: {next_student} is next.")

    def reserve_book(self, book_id, student):
        if book_id not in self.books_by_id:
            print("Book not found.")
            return
        self.reservations[book_id].append(student)
        print(f"Reservation added for {student}.")

    def process_reservation(self, book_id):
        if book_id not in self.books_by_id:
            print("Book not found.")
            return
        queue = self.reservations[book_id]
        if not queue:
            print("No reservations for this book.")
            return
        if not self.books_by_id[book_id].available:
            print("Book is currently issued. Process reservation after it is returned.")
            return
        student = queue.popleft()
        self.issue_book(book_id, student)
        print(f"Processed the oldest reservation for {student}.")

    def display_sorted_books(self):
        books = []
        current = self.head
        while current:
            books.append(current.book)
            current = current.next
        # Merge sort: O(n log n)
        sorted_books = self._merge_sort(books)
        if not sorted_books:
            print("No books in the library.")
        for book in sorted_books:
            print(book)

    def _merge_sort(self, items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = self._merge_sort(items[:mid])
        right = self._merge_sort(items[mid:])
        return self._merge(left, right)

    @staticmethod
    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].title.lower() <= right[j].title.lower():
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
