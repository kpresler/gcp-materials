# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 11:15:40 2025

@author: Kai
"""

class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False
        
    def check_out(self):
        self.checked_out = True
        
    def check_in(self):
        self.checked_out = False
        
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
        
    def __repr__(self):
        return str(self)
        
# Create a book instance
book1 = Book("Python Programming", "John Smith", "978-1234567890")
# Check out the book
book1.check_out()
# Check the book's status
print(book1.checked_out) # Expected output: True
# Check in the book
book1.check_in()
# Check the book's status
print(book1.checked_out) # Expected output: False



class Member:
    
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.checked_out_books = list()
        
        
    def check_out_book(self, book):
        self.checked_out_books.append(book)
        book.check_out()
        
    def return_book(self, book):
        self.checked_out_books.remove(book)
        book.check_in()
        

# Create a member instance
member1 = Member("M001", "Alice")

# Check out a book
member1.check_out_book(book1)
# Check the member's checked-out books
print(member1.checked_out_books) # Expected output: [book1]
# Return a book
member1.return_book(book1)
# Check the member's checked-out books
print(member1.checked_out_books) # Expected output: 
    
    
class Library:
    
    def __init__(self):
        self.books = list()
        
    def add_book(self, book):
        self.books.append(book)
    
    def search_book(self, search_term):
        
        found_books = list()
        
        for book in self.books:
            
            if search_term in book.title or search_term in book.author:
                found_books.append(book)
                
        return found_books
    
    def display_books(self):
        for book in self.books:
            print(book)
            
            
            
# Create a second book instance
book2 = Book("Data Science Handbook", "Alice Johnson", "978-9876543210")
# Create a library instance
library = Library()
# Add books to the library
library.add_book(book1)
library.add_book(book2)
# Search for books by title
found_books = library.search_book("Python")
print(found_books) # Expected output: [book1]
# Display all books in the library
library.display_books()


class Transaction:
    
    transactions = list()
    
    
    @classmethod
    def record_transaction(cls, member, book, action):
        
        cls.transactions.append(f"{member.name} {action} {book}")
        
member2 = Member("M002", "Bob")
# Record transactions
Transaction.record_transaction(member1, book1, "checked out")
Transaction.record_transaction(member2, book2, "checked out")
Transaction.record_transaction(member1, book1, "returned")
# Display transaction history
for transaction in Transaction.transactions:
    print(transaction)
# Expected output:
# Alice checked out 'Python Programming' (ISBN: 978-1234567890)
# Bob checked out 'Data Science Handbook' (ISBN: 978-9876543210)
# Alice returned 'Python Programming' (ISBN: 978-1234567890