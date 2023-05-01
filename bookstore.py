# =================================== CAPSTONE PROJECT: BOOKSTORE ===================================

import sqlite3

# Create a database called ebookstore
db = sqlite3.connect('ebookstore')

cursor = db.cursor()

# Create a table called books
cursor.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
''')
db.commit()

book_data = [(3001, "A Tale of Two Cities", "Charles Dickens", 30), (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40), (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25), (3004, "The Lord of the Rings", "J.R.R Tolkien", 37), (3005, "Alice in Wonderland", "Lewis Carroll", 12)]

# Insert rows from book_data
cursor.executemany('''INSERT INTO books VALUES(?,?,?,?)''', book_data)
db.commit()

# Enter a new book function
def enter_book():
      id_ = int(input("Enter the book ID: "))
      title_ = input("Enter the book ttle: ")
      author_ = input("Enter the book author: ")
      qty_ = int(input("Enter the quantity of books: "))
      cursor.execute('''INSERT INTO books(id, title, author, qty) VALUES(?,?,?,?)''', (id_, title_, author_, qty_))
      db.commit()
      print("Book successfully entered.")

# Update a book function
def update_book():
    id_ = int(input("Enter the ID of the book you would like to update: "))

    # Check if the book exists in the database
    cursor.execute("SELECT * FROM books WHERE id = ?", (id_,))
    book = cursor.fetchone()
    if book is None:
        print("Book not found in the database.")
        return
    
    choice = input('''
    What would you like to update (select 1, 2, or 3):
    1.  Title
    2.  Author
    3.  Quantity''').strip()
    if choice == "1":
        title_ = input("Enter the updated title: ")
        cursor.execute('''UPDATE books SET title = ? WHERE title = ?''', (title_, id_))
        db.commit()
        print("Book title updated.")
    elif choice == "2":
        author_ = input("Enter the updated author: ")
        cursor.execute('''UPDATE books SET author = ? WHERE id = ?''', (author_, id_))
        db.commit()
        print("Book author updated.")
    elif choice == "3":
        qty_ = int(input("Enter the updated quantity of books in stock: "))
        cursor.execute('''UPDATE books SET qty = ? WHERE id = ?''', (qty_, id_))
        db.commit()
        print("Book quantity updated.")
    else:
        print("Oops! Invalid entry.")

# Delete a book function
def delete_book():
    id_ = int(input("Enter the ID of the book to delete: "))
    # Check if the book exists in the database
    cursor.execute("SELECT * FROM books WHERE id = ?", (id_,))
    book = cursor.fetchone()
    if book is None:
        print("Book not found in the database.")
        return
    
    cursor.execute('''DELETE FROM books WHERE id = ?''', (id_,))
    db.commit()
    print("Book deleted.")

# Search a book function by title or author
def search_book():
    choice = int(input('''
    Enter the book ID: ''').strip())
        # Check if the book exists in the database
    cursor.execute("SELECT * FROM books WHERE id = ?", (id_,))
    book = cursor.fetchone()
    if book is None:
        print("Book not found in the database.")
        return
    
    cursor.execute('''SELECT id, title, author, qty FROM books WHERE id = ?''', (choice,))
    book = cursor.fetchone()
    print(book)

# Display menu options to user
while True:
    user_choice = input('''
Welcome to the ebookstore database management system!
Enter the number to select the action
1. Enter book
2. Update book
3. Delete book
4. Search books
5. Exit
:
    ''').strip()

    if user_choice == "1":
        enter_book()
    elif user_choice == "2":
        update_book()
    elif user_choice == "3":
        delete_book()
    elif user_choice == "4":
        search_book()
    elif user_choice == "5":
        db.close()
        print("Connection to database closed.")
        exit()
    else:
        print("Whoops! Invalid input. Try again.")