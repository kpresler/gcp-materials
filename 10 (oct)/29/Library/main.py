# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 11:15:56 2025

@author: Kai
"""

from library import Book, Member, Library, Transaction

# Create library instance
library = Library()

# Create books
book1 = Book("Python Programming", "John Smith", "978-1234567890")
book2 = Book("Data Science Handbook", "Alice Johnson", "978-9876543210")
book3 = Book("Web Development Basics", "Bob Brown", "978-1111111111")

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create library members
member1 = Member("M001", "Alice")
member2 = Member("M002", "Bob")

# Member checks out books
member1.check_out_book(book1)
member2.check_out_book(book2)

# Member returns books
member1.return_book(book1)
member2.return_book(book2)

# Search for books
found_books = library.search_book("Python")
print("Books matching 'Python':")
library.display_books()

# Record transactions
Transaction.record_transaction(member1, book1, "checked out")
Transaction.record_transaction(member2, book2, "checked out")
Transaction.record_transaction(member1, book1, "returned")

# Display transactions
print("\nTransaction History:")
for transaction in Transaction.transactions:
    print(transaction)
