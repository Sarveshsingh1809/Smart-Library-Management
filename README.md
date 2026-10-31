# Smart Library Management System

A beginner-friendly, console-based Python mini-project demonstrating core Data Structures and Algorithms (DSA).

## Features
- Add and remove books
- Search by book ID or partial title
- Display all books
- Issue and return books
- Queue book reservations using FIFO order
- Sort books alphabetically using merge sort

## DSA Concepts
| Concept | Implementation | Purpose |
|---|---|---|
| Singly linked list | `Node`, `Library.head` | Store and traverse book records |
| Hash table | `books_by_id` dictionary | Fast average O(1) lookup by ID |
| Queue | `collections.deque` | FIFO reservation requests |
| Merge sort | `_merge_sort()` | Sort titles in O(n log n) time |
| Linear search | Linked-list title traversal | Find a title or partial title |

## Requirements
- Python 3.8 or later
- No third-party packages required

## Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

## Example
```text
===== SMART LIBRARY MANAGEMENT SYSTEM =====
1. Add book
2. Remove book
3. Search book
4. Display all books
5. Issue book
6. Return book
7. Reserve book
8. Process reservation
9. Sort books by title
0. Exit
Choose an option: 1
Book ID: B101
Title: Data Structures
Author: Mark Allen
Book added successfully.
```

## Future Improvements
- Save data to a JSON or SQLite database
- Add student IDs and due dates
- Build a GUI using Tkinter
- Add unit tests

## License
This project is provided for educational use.
