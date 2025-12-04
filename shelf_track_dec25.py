# Import libraries
import sqlite3

# =========================================================================
# === Functions ===

# --------------------------------------------------------------------------
# Prepare ebookstore database functions


def load_stock_from_file(filepath):
    '''
    This function reads book data from a text file and returns it as a
    list of tuples in the same format as the stock list.
    Expected file format (one book per line):
    id,title,authorID,qty
    Example:
    3001,A Tale of Two Cities,1290,30
    '''
    stock = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, start=1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue  # skip empty lines and comments
                try:
                    parts = line.split(',')
                    if len(parts) != 4:
                        print(f"Skipping line {line_num}: incorrect format")
                        continue
                    book_id = int(parts[0].strip())
                    title = parts[1].strip()
                    author_id = int(parts[2].strip())
                    qty = int(parts[3].strip())
                    stock.append((book_id, title, author_id, qty))
                except ValueError:
                    print(f"Skipping line {line_num}: invalid data")
        print(f"Loaded {len(stock)} books from {filepath}.")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    return stock


def export_books_to_file(cursor, filepath):
    '''
    This function exports all books from the database to a text file
    in CSV format (id,title,authorID,qty).
    Parameters:
        cursor = database cursor object
        filepath = path where the file should be saved
    '''
    import os

    try:
        cursor.execute('SELECT id, title, authorID, qty FROM book')
        books = cursor.fetchall()

        if not books:
            print("No books in database to export.")
            return False

        # Check if file exists and get user confirmation
        if os.path.exists(filepath):
            confirm = input(f"File '{filepath}' already exists. "
                            f"Overwrite? (y/n): ").lower()
            if confirm != 'y':
                print("Export cancelled.")
                return False

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write("# Book data exported from ebookstore.db\n")
            file.write("# Format: id,title,authorID,qty\n")
            for book in books:
                line = f"{book[0]},{book[1]},{book[2]},{book[3]}\n"
                file.write(line)

        print(f"Successfully exported {len(books)} books to {filepath}")
        return True
    except Exception as e:
        print(f"Error exporting books: {e}")
        return False


def initialise_ebookstore_db(cursor):
    '''
    This function initialises the tables for ebookstore.db and
    initialises a cursor object for use throughout the program.
    '''
    # Create book table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS book(
                id INTEGER PRIMARY KEY,
                title TEXT,
                authorID INTEGER,
                qty INTEGER)
                ''')
    # Create author table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS author(
                id INTEGER PRIMARY KEY,
                name TEXT,
                country TEXT)
                ''')
    db.commit()


def populate_book_table(cursor, stock=None):
    '''
    This function checks if the book table exists, then populates the
    table if it is empty. Optionally accepts a stock list; if None,
    uses default stock data.
    '''
    if stock is None:
        stock = [
            (3001, "A Tale of Two Cities", 1290, 30),
            (3002, "The Left Hand of Darkness", 8937, 40),
            (3003, "The Lion the Witch and the Wardrobe", 2356, 25),
            (3004, "The Lord of the Rings", 6380, 37),
            (3005, "Alice's Adventures in Wonderland", 5620, 12),
            (3006, "The Long Way to a Small Angry Planet", 2001, 27)
            ]
    # Check if empty
    try:
        cursor.executemany('''
                           INSERT INTO book(id, title, authorID, qty)
                           VALUES(?, ?, ?, ?)
                           ''',
                           stock
                           )
        print("Sample book table populated and loaded.")
        db.commit()
    except sqlite3.IntegrityError:
        print('Book table loaded.')


def populate_author_table(cursor):
    '''
    This function checks if the author table exists, then populates
    the table if it is empty.
    '''
    author_info = [
        (1290, "Charles Dickens", "England"),
        (8937, "Ursula K. Le Guin", "California"),
        (2356, "C.S. Lewis", "Ireland"),
        (6380, "J.R.R. Tolkien", "South Africa"),
        (5620, "Lewis Carroll", "England"),
        (2001, "Becky Chambers", "California")
        ]
    # Check if empty
    try:
        cursor.executemany('''
                           INSERT INTO author(id, name, country)
                           VALUES(?, ?, ?)
                           ''',
                           author_info
                           )
        print("Empty author table populated and loaded.")
        db.commit()
    except sqlite3.IntegrityError:
        print("Author table loaded.")


def prepare_ebookstore_db(cursor):
    '''
    This function initialises the tables for ebookstore.db and
    populates them with data if they are empty. Asks the user if they
    want to load custom data from a file.
    '''
    initialise_ebookstore_db(cursor)

    # Ask user if they want to load from file
    user_choice = input('''Would you like to load book data from a file?
Enter 'y' to load from file or any other key to use default data
: ''').lower()

    custom_stock = None
    if user_choice == 'y':
        filepath = input("Enter the filepath for the book data file: ")
        custom_stock = load_stock_from_file(filepath)
        if custom_stock is None:
            print("Failed to load custom data. Using default data instead.")

    populate_book_table(cursor, custom_stock)
    populate_author_table(cursor)


# ------------------------------------------------------------------------
# Display functions


def display_all_books(query_str):
    '''
    This function displays a summary of the entire book inventory on
    the screen.
    '''
    cursor.execute(query_str)
    book_list = cursor.fetchall()

    # Display the inventory if any books are selected for display
    if book_list:
        print("Book inventory")
        print(" id  : title : author : qty")
        for book in book_list:
            print(f"{book[0]} : {book[1]} : {book[2]} : {book[3]}")
    else:
        print("No books found.")


def display_books_cond(query_str, condition):
    '''
    This function displays a summary of the book inventory matching a
    condition on the screen.
    '''
    cursor.execute(query_str, (condition,))
    book_list = cursor.fetchall()

    # Display the inventory if any books are selected for display
    if book_list:
        print("Book inventory")
        print(" id  : title : author : qty")
        for book in book_list:
            print(f"{book[0]} : {book[1]} : {book[2]} : {book[3]}")
    else:
        print("No books found.")


# -------------------------------------------------------------------------
# Select book functions


def select_book():
    '''
    This function displays all the books and asks the user to enter a
    book id. It returns the selected_bk record.
    '''
    # Display the books
    query_str = '''
                SELECT book.id, book.title, author.name, book.qty
                FROM book INNER JOIN author
                ON book.authorID = author.id
                '''
    display_all_books(query_str)

    # Get user input and select the corresponding book
    while True:
        try:
            input_id = int(input("Select a book.\nEnter its id number: "))
            cursor.execute('''
                   SELECT book.id, book.title,
                   author.id, author.name, author.country,
                   book.qty
                   FROM book INNER JOIN author
                   ON book.authorID = author.id
                   WHERE book.id = ?''', (input_id,))

            # Display selected book details
            selected_bk = cursor.fetchone()
            if selected_bk is None:
                print(f"No book found with id {input_id}. Please try again.")
            else:
                print(f"Selected book summary\n\nid : title"
                      f"\n{selected_bk[0]} : {selected_bk[1]}"
                      f"\n\nauthorID : author name : country"
                      f"\n{selected_bk[2]} : {selected_bk[3]} : "
                      f"{selected_bk[4]}"
                      f"\n\nquantity: {selected_bk[5]}\n"
                      )
            break  # out of while loop
        except ValueError:
            print("Please enter a four digit book id number.")
    return selected_bk


# --------------------------------------------------------------------------
# Input field functions


def input_title(cursor):
    '''
    This function checks if a title is unique. If not, it asks the user
    if they want to continue with the duplicate title or enter a new
    one.
    '''
    bk_title = input("Title: ")
    # Check the entered title is unique
    cursor.execute('''
                SELECT book.id, book.title,
                author.id, author.name, author.country,
                book.qty
                FROM book INNER JOIN author
                ON book.authorID = author.id
                WHERE book.id = ?''', (bk_title,))
    test_unique = cursor.fetchone()

    if test_unique is not None:  # Title is a duplicate
        print(f"A book with {bk_title} already exists."
              f"\nEnter 'y' to accept this title or any other key "
              f"to try again.")
        confirm_existing_title = input(": ")
        # Allow for upper or lower case input while avoiding exceptions
        # if the user doesn't input a letter.
        if confirm_existing_title == 'y' or confirm_existing_title == 'Y':
            return bk_title
        else:
            input_title(cursor)

    else:  # Title is unique
        return bk_title


def input_book_id(cursor):
    '''
    This function checks if a book id is a four digit number and is
    unique.
    '''
    # Check the entered id is a four digit number
    while True:
        try:
            bk_id = int(input("Book id: "))
            if bk_id >= 1000 and bk_id <= 9999:
                break  # out of while loop
            else:
                print("Please enter a four digit number greater than 999.")
        except ValueError:
            print("Please enter a four digit number greater than 999.")

    # Check the entered id is unique
    cursor.execute('''
                SELECT *
                FROM book
                WHERE book.id = ?''', (bk_id,))
    test_unique = cursor.fetchone()

    if test_unique is not None:  # id is a duplicate
        print(f"Book id {bk_id} is assigned to {test_unique[1]}."
              f"\nPlease try again.")
        input_book_id(cursor)
    else:  # id is unqiue
        return bk_id


def input_author_id(cursor):
    '''
    This function checks if an authorID is a four digit number and is
    unique. If not, it asks the user if they want to continue with the
    repeated author or enter a new one.
    '''
    # Check the entered authorID is a four digit number
    while True:
        try:
            auth_id = int(input("authorID: "))
            if auth_id >= 1000 and auth_id <= 9999:
                break  # out of while loop
            else:
                print("Please enter a four digit number greater than 999.")
        except ValueError:
            print("Please enter a four digit number greater than 999.")

    # Check the entered authorID is unique
    cursor.execute('''
                SELECT book.id, book.title,
                author.id, author.name, author.country,
                book.qty
                FROM book INNER JOIN author
                ON book.authorID = author.id
                WHERE author.id = ?''', (auth_id,))
    test_unique = cursor.fetchone()

    # Allow for the case where an author has written more than one book.
    if test_unique is not None:  # authorID is a duplicate
        print(f"authorID {auth_id} is assigned to {test_unique[3]}."
              f"\nEnter 'y' to accept this author or any other key "
              f"to try again.")
        confirm_existing_author = input(": ")
        # Allow for upper or lower case input while avoiding exceptions
        # if the user doesn't input a letter.
        if confirm_existing_author == 'y' or confirm_existing_author == 'Y':
            db.commit()
            return auth_id
        else:
            input_author_id(cursor)

    else:  # authorID is unique
        db.commit()
        return auth_id


def input_author_details(cursor, auth_id):
    '''
    This function checks if a valid authorID is linked to name and country.
    If there is a link, the author data is returned: author_data = [authorID,
    name, country]. If there isn't a link, the user is asked to input
    name and country to complete author_data.
    '''
    # Count the records in book table containing auth_id
    cursor.execute('''
                   SELECT COUNT()
                   FROM book
                   WHERE book.authorID = ?''',
                   (auth_id,)
                   )
    auth_count = cursor.fetchone()

    # Get the author information
    cursor.execute('''
                    SELECT author.id, author.name, author.country
                    FROM author
                    WHERE author.id = ?''', (auth_id,))
    author_data = cursor.fetchone()

    # authorID is created by input_author_id, which has checked the authorID
    # is unique or assigned to an existing author. If the authorID is unique
    # it is created as a new entry in the author table, without any
    # accompanying information. If the count of authorID in the book table
    # is 0, ask the user to input name and country. Otherwise, return
    # the existing record in author_data.
    if auth_count[0] == 0:
        author_data = []
        author_data.append(auth_id)
        author_data.append(input("Author name: "))
        author_data.append(input("Author country: "))
    # else the author exists and return the existing complete record
    return author_data


def input_book_qty():
    '''
    This function asks the user to enter a qty and checks the input is
    a number. It returns bk_qty as int.
    '''
    while True:
        try:
            bk_qty = int(input("Quantity: "))
            break  # out of the while loop
        except ValueError:
            print("Please enter a number.")
    return bk_qty


# ---------------------------------------------------------------------------
# 1 Enter book functions


def enter_book():
    '''
    This function takes input from the user needed to enter a book into
    the database and INSERTs the record.
    '''
    # Get user inputs and check validity
    print("Enter a book into the database."
          "\nPlease enter the book information."
          )
    # Call input functions
    bk_title = input_title(cursor)
    bk_qty = input_book_qty()
    bk_id = input_book_id(cursor)
    auth_id = input_author_id(cursor)
    author_data = input_author_details(cursor, auth_id)
    # Extract fields from the list returned by author_data
    auth_name = author_data[1]
    auth_country = author_data[2]

    # Insert the new book record into the database
    cursor.execute('''
                   INSERT INTO book(id, title, authorID, qty)
                   VALUES (?, ?, ?, ?)''',
                   (bk_id, bk_title, auth_id, bk_qty)
                   )
    db.commit()
    print(f"{bk_title} entered into database.")

    # Insert a new author record into the database, unless the author
    # already exists.
    try:
        cursor.execute('''
                    INSERT INTO author(id, name, country)
                    VALUES (?, ?, ?)''', (auth_id, auth_name, auth_country))
        db.commit()
        print(f"{auth_name} entered into database.")
    except sqlite3.IntegrityError:
        print("Author information confirmed present in database.")

    # Display updated book inventory
    query_str = '''
                SELECT book.id, book.title, author.name, book.qty
                FROM book INNER JOIN author
                ON book.authorID = author.id
                '''
    display_all_books(query_str)


# --------------------------------------------------------------------------
# 2 Update book functions


def update_title(selected_bk):
    '''
    This function updates the title of a book based on user input. It is
    called by update_book(). Duplicate titles are allowed.
    '''
    input_title = input("Enter the updated title: ")
    cursor.execute('''
                    UPDATE book SET title = ?
                    WHERE id = ?''', (input_title, selected_bk[0]))
    db.commit()
    print(f"Title of book {selected_bk[0]} updated to:\n{input_title}.")


def update_auth_name(selected_bk):
    '''
    This function asks the user for an updated author name. Then it
    checks if the name is unique or not. If the updated author name
    already exists in the database, the authorID for the book is
    set to the value in the database and the record is repopulated.
    If the updated author name is unique, it is simply added to the
    database.
    '''

    updated_name = input("Enter the updated author name: ")
    # Check updated_name is unique
    cursor.execute('''
                SELECT book.id, book.title,
                author.id, author.name, author.country,
                book.qty
                FROM book INNER JOIN author
                ON book.authorID = author.id
                WHERE author.name = ?''', (updated_name,))
    test_unique = cursor.fetchone()

    # Allow for the case where an author has written more than one book.
    if test_unique is not None:  # the author already exists
        print(f"{updated_name} already exists in the database.")
        auth_country = test_unique[4]
        print(f"{updated_name}'s country is {auth_country}.")

        # Update the book record to have the existing authorID
        # and repopulate the author information
        selected_auth_id = test_unique[2]
        cursor.execute('''
                        UPDATE book SET authorID = ?
                        WHERE id = ?''', (selected_auth_id, selected_bk[0]))
        db.commit()

    else:  # the author is unique
        selected_auth_id = selected_bk[2]
        cursor.execute('''
                       UPDATE author SET name = ?
                       WHERE id = ?''', (updated_name, selected_auth_id))
        db.commit()

    print(f"Author of book {selected_bk[1]} "
          f"updated to\n{updated_name}.")


def update_author(selected_bk):
    '''
    This function updates the author information of a book based on
    user input. It is called by update_book().
    '''
    selected_auth_id = selected_bk[2]  # authorID

    # Count the records in book containing selected_auth_id
    cursor.execute('''
                SELECT COUNT()
                FROM book
                WHERE book.authorID = ?''', (selected_auth_id,))
    auth_count = cursor.fetchone()

    # If the author appears against more than one book ask if the
    # user wants to update the selected book or all books by that author.
    # If there is only one book by the selected author, the user can update
    # the author information directly.
    if auth_count[0] > 1:
        update_all = input("Enter 'y' to update this author "
                           "information for all books with this author"
                           "\n or any other key to cancel: ")
        # Allow for upper or lower case input while avoiding exceptions
        # if the user doesn't input a letter.
        if update_all == 'y' or update_all == 'Y':
            print("Update this author information for all their books.")
        else:
            print("To update the author of multiple books for one book only "
                  "delete this book and enter it again.")
            return  # to main menu

    # Update author submenu if the user wants to update the author information
    # for all books by that author.
    while True:
        update_author_menu = input('''Enter '1' to update author name
or enter '2' to update author country
or any other key to go back to the main menu
: ''')

        if update_author_menu == '1':
            update_auth_name(selected_bk)

        elif update_author_menu == '2':
            updated_country = input("Enter the updated author country: ")
            cursor.execute('''
                        UPDATE author SET country = ?
                        WHERE id = ?''', (updated_country, selected_auth_id))
            db.commit()
            print(f"Author country of book {selected_bk[1]} "
                  f"updated to\n{updated_country}.")
        else:
            break  # out of while loop


def update_qty(input_qty, selected_bk):
    '''
    This function updates the quantity of a book based on user input.
    It is called by update_book().
    '''
    cursor.execute('''
                    UPDATE book SET qty = ?
                    WHERE ID = ?''', (input_qty, selected_bk[0]))
    db.commit()
    print(f"Quantity of book {selected_bk[1]} updated to\n{input_qty}.")


def update_book():
    '''
    This function asks a user to select a book by entering the id and
    UPDATEs one of the fields in the database. If the user enters a
    number, the quantity updates by default. Alternatively the user can
    enter letters to update the title or authorID.
    '''
    selected_bk = select_book()
    if selected_bk is not None:
        submenu = input('''========== Update Submenu ==========
Enter the updated quantity or
enter 't' to update the title or
enter 'a' to update the author name and country or
enter 'x' to cancel the operation
: ''').lower()

        if submenu == 't':
            update_title(selected_bk)

        elif submenu == 'a':
            update_author(selected_bk)

        elif submenu == 'x':
            print("Operation cancelled.")

        else:
            try:
                input_qty = int(submenu)
                update_qty(input_qty, selected_bk)
            except ValueError:
                print("Invalid input. Please try again.")
    else:
        print("No books found")


# ---------------------------------------------------------------------
# 3 Delete book functions


def delete_book():
    '''
    This function asks a user to select a book by entering the id and
    DELETEs it from the database. If the author is unqiue, the author
    record is also deleted. If the author is not unique, the author
    record is retained.
    '''
    while True:
        selected_bk = select_book()
        # Get book information
        if selected_bk is not None:
            selected_bk_id = selected_bk[0]
            selected_auth_id = selected_bk[2]
            selected_author = selected_bk[3]
        else:  # book does not exist
            print("No books found")
            break  # out of while loop

        # Confirm the operation
        confirm = input("To delete this book enter 'y' or any "
                        "other key to cancel: ")
        # Allow for upper or lower case input while avoiding exceptions
        # if the user doesn't input a letter.
        if confirm == 'y' or confirm == 'Y':
            cursor = db.cursor()
            cursor.execute('''
                        DELETE FROM book WHERE id = ?''', (selected_bk_id,))
            output_str = f"{selected_bk_id} {selected_bk[1]} deleted."

            # Delete the author information if the author is unique.
            # Uses sqlite COUNT (Geeks for geeks, 2023b)
            cursor.execute('''
                            SELECT COUNT(book.authorID)
                            FROM book
                            WHERE authorID = ?''', (selected_auth_id,))
            author_count = cursor.fetchone()

            if author_count[0] == 0:  # author is unique
                cursor.execute('''
                            DELETE FROM author WHERE id = ?''',
                               (selected_auth_id,))
                output_str += f"\n{selected_author} deleted."

            else:  # author is not unique
                output_str += f"\n{selected_author} remains in "
                output_str += "the database."

            db.commit()
            print(output_str)

            # Display updated inventory
            query_str = '''
                SELECT book.id, book.title, author.name, book.qty
                FROM book INNER JOIN author
                ON book.authorID = author.id
                '''
            display_all_books(query_str)
            break  # out of while loop

        else:
            print('Operation cancelled.')
            break  # out of while loop


# --------------------------------------------------------------------------
# 4 Search book functions


def search_book_title(input_search):
    '''
    This function takes user input to search for a book by title.
    It makes use of the LIKE operator (Geeks for Geeks, 2023a) and
    wildcards to allow for incomplete titles. However it doesn't allow
    searching for just the keywords in a title eg 'tale' or 'cities' will
    return A Tale of Two Cities but 'tale cities' returns None.
    '''

    search_title = '%' + input_search + '%'
    # Search and display the results
    query_str = '''SELECT book.id, book.title, author.name, book.qty
                FROM book INNER JOIN author
                ON book.authorID = author.id
                WHERE title LIKE ?'''
    display_books_cond(query_str, search_title)


def search_book_id():
    '''
    This function is triggered by a user input to search for book by id.
    I expect the title search to be more common, but there may be
    instances where a user has the id but isn't certain of the title,
    so I included this function as an option for completeness.
    '''

    # Check the entered id is a four digit number
    while True:
        try:
            search_id = int(input("Enter the book id to search for: "))
            if search_id >= 1000 and search_id <= 9999:
                break  # out of while loop
            else:
                print("Please enter a four digit number greater than 999.")
        except ValueError:
            print("Please enter a four digit number greater than 999.")

    # Search and display the results
    query_str = '''SELECT book.id, book.title, author.name, book.qty
                   FROM book INNER JOIN author
                   ON book.authorID = author.id
                   WHERE book.id = ?'''
    display_books_cond(query_str, search_id)


def search_author(input_search):
    '''
    This function is triggered by a user input to search by author.
    '''
    search_name = '%' + input_search + '%'

    # Search and display the results
    query_str = '''SELECT book.id, book.title, author.name, book.qty
                   FROM book INNER JOIN author
                   ON book.authorID = author.id
                   WHERE author.name LIKE ?'''
    display_books_cond(query_str, search_name)


def search_book():
    '''
    This function asks for user input to search the books. By default it
    searches by title, but the user can choose to search by book id or
    authorID if they wish.
    '''
    input_search = input('''Enter the title to search for:
    or enter 'a' to search by author
    or enter 10 to search by book id
    : ''')
    if input_search == '10':
        search_book_id()
    elif input_search == 'a':
        input_search = input("Enter author name: ")
        search_author(input_search)
    else:
        search_book()


# -------------------------------------------------------------------------
# 5 View details of all books functions


def detail(item):
    '''
    This function displays the details of an individual book in the
    required format. It is called by view_details().
    '''
    detail_str = f"\nTitle: {item[0]}"
    detail_str += f"\nAuthor\'s Name: {item[1]}"
    detail_str += f"\nAuthor\'s Country: {item[2]}"
    detail_str += "\n-----------------------------------------------------"
    return detail_str


def view_details():
    '''
    This function uses an INNER JOIN to find information from both
    book and author tables. It outputs to the screen in the required
    format.
    '''
    # Prepare header for output
    header = "Details"
    header += "\n-----------------------------------------------------"
    print(header)

    # Get the detail information and display to screen
    cursor = db.cursor()
    cursor.execute('''
                   SELECT book.title, author.name, author.country
                   FROM book INNER JOIN author
                   ON book.authorID = author.id
                   ''')
    detail_list = cursor.fetchall()
    for item in detail_list:
        print(detail(item))


# =========================================================================
# === Main program ===

# Connect database
db = sqlite3.connect('ebookstore.db')

# Create cursor object
cursor = db.cursor()

prepare_ebookstore_db(cursor)

# === Main Menu ===
while True:
    menu = int(input(
        '''============= Main Menu ============
Select one of the following options:
    1 - Enter book
    2 - Update book
    3 - Delete book
    4 - Search books
    5 - View details of all books
    6 - Export books to file
    0 - Exit
'''
    ))

    if menu == 1:
        enter_book()

    elif menu == 2:
        update_book()

    elif menu == 3:
        delete_book()

    elif menu == 4:
        search_book()

    elif menu == 5:
        view_details()

    elif menu == 6:
        export_path = input("Enter the filepath to save books "
                            "(e.g., my_books.txt): ")
        export_books_to_file(cursor, export_path)

    elif menu == 0:
        # Close database
        db.commit()  # Just in case there are any uncommitted changes
        db.close()
        print("Database disconnected.\n")
        print("Goodbye!")
        exit()

    else:
        print("You have entered an invalid input. Please try again.")

# ==========================================================================
#
# References
#
# Geeks for geeks (2023a)
# https://www.geeksforgeeks.org/sql/sql-query-to-match-any-part-of-string/
#
# Geeks for geeks (2023b)
# https://www.geeksforgeeks.org/sqlite/sqlite-count/
#
# Index (2025)
# https://www.index.dev/blog/python-database-error-handling-try-except
#
# Real Python (2024)
# https://realpython.com/python-zip-function/#understanding-the-python-zip-function
