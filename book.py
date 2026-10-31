class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        self.issued_to = None

    def __str__(self):
        status = "Available" if self.available else f"Issued to {self.issued_to}"
        return f"ID: {self.book_id} | {self.title} | {self.author} | {status}"
