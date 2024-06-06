# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('bookhaven.db')
# cursor = conn.cursor()

# # Create Books table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Books (
#         book_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         isbn TEXT UNIQUE NOT NULL,
#         genre TEXT,
#         publication_year INTEGER,
#         author_id INTEGER,
#         FOREIGN KEY (author_id) REFERENCES Authors (author_id)
#     )
# ''')

# # Create Authors table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Authors (
#         author_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         birthdate DATE,
#         collaborator_id INTEGER,
#         FOREIGN KEY (collaborator_id) REFERENCES Authors (author_id)
#     )
# ''')

# # Create Customers table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Customers (
#         customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT NOT NULL,
#         last_name TEXT NOT NULL,
#         email TEXT UNIQUE NOT NULL,
#         phone TEXT
#     )
# ''')

# # Create Transactions table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Transactions (
#         transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         transaction_date DATE NOT NULL,
#         customer_id INTEGER,
#         book_id INTEGER,
#         quantity INTEGER NOT NULL,
#         total_price REAL NOT NULL,
#         FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
#         FOREIGN KEY (book_id) REFERENCES Books (book_id)
#     )
# ''')

# # Commit changes and close the connection
# conn.commit()
# conn.close()





# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('autorent.db')
# cursor = conn.cursor()

# # Create Vehicles table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Vehicles (
#         vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         make TEXT NOT NULL,
#         model TEXT NOT NULL,
#         year INTEGER,
#         registration_number TEXT UNIQUE NOT NULL,
#         rental_agreement_id INTEGER UNIQUE,
#         FOREIGN KEY (rental_agreement_id) REFERENCES Rental_Agreements (rental_agreement_id)
#     )
# ''')

# # Create Rental_Agreements table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Rental_Agreements (
#         rental_agreement_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         agreement_date DATE NOT NULL,
#         customer_id INTEGER,
#         vehicle_id INTEGER UNIQUE,
#         rental_period INTEGER NOT NULL,
#         total_cost REAL NOT NULL,
#         FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
#         FOREIGN KEY (vehicle_id) REFERENCES Vehicles (vehicle_id)
#     )
# ''')

# # Commit changes and close the connection
# conn.commit()
# conn.close()






# import sqlite3

# def create_bookhaven_db():
#     conn = sqlite3.connect('bookhaven.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Books (
#             book_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL,
#             isbn TEXT UNIQUE NOT NULL,
#             genre TEXT,
#             publication_year INTEGER,
#             author_id INTEGER,
#             FOREIGN KEY (author_id) REFERENCES Authors (author_id)
#         )
#     ''')

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Authors (
#             author_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             birthdate DATE,
#             collaborator_id INTEGER,
#             FOREIGN KEY (collaborator_id) REFERENCES Authors (author_id)
#         )
#     ''')

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Customers (
#             customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             phone TEXT
#         )
#     ''')

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Transactions (
#             transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             transaction_date DATE NOT NULL,
#             customer_id INTEGER,
#             book_id INTEGER,
#             quantity INTEGER NOT NULL,
#             total_price REAL NOT NULL,
#             FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
#             FOREIGN KEY (book_id) REFERENCES Books (book_id)
#         )
#     ''')

#     conn.commit()
#     conn.close()

# def create_autorent_db():
#     conn = sqlite3.connect('autorent.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Vehicles (
#             vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             make TEXT NOT NULL,
#             model TEXT NOT NULL,
#             year INTEGER,
#             registration_number TEXT UNIQUE NOT NULL,
#             rental_agreement_id INTEGER UNIQUE,
#             FOREIGN KEY (rental_agreement_id) REFERENCES Rental_Agreements (rental_agreement_id)
#         )
#     ''')

#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Rental_Agreements (
#             rental_agreement_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             agreement_date DATE NOT NULL,
#             customer_id INTEGER,
#             vehicle_id INTEGER UNIQUE,
#             rental_period INTEGER NOT NULL,
#             total_cost REAL NOT NULL,
#             FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
#             FOREIGN KEY (vehicle_id) REFERENCES Vehicles (vehicle_id)
#         )
#     ''')

#     conn.commit()
#     conn.close()

# # Create both databases
# create_bookhaven_db()
# create_autorent_db()