# Python Data Structure Challenges in Real-World Scenarios
# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

def add_book_to_library(library, new_book):
    
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{new_book[0]}' by {new_book[1]} added to the library.")
    else:
        print(f"Book '{new_book[0]}' by {new_book[1]} already exists in the library.")
    
    return library

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

new_books = [("Fire and Blood", "George R.R. Martin"), ("Harry Potter", "J.K. Rowling")]

for book in new_books:
    library = add_book_to_library(library, book)

print("Updated Library:", library)