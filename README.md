# Ebookstore — SQL Inventory and Menu-Driven Database Application

This project showcases the application of **SQL within a Python program** to manage an ebookstore’s inventory and operations. Completed as part of my data science bootcamp, this task helped me explore how relational databases support real-world workflows — from adding new books to querying existing inventory — and how to integrate SQL logic with Python for a complete solution.

I was genuinely excited by the logical elegance of SQL and how database design decisions directly shape query behaviour. The project reflects both this enthusiasm and a disciplined approach to solving a practical problem with code.

![Ornate, multi-level bookstore with carved wooden railings, tall bookshelves filled with books, warm lighting from hanging lanterns, and a grand central staircase leading between floors. The tonal palette is warm and autumnal.](https://github.com/SarennahL-C/pf-ebookstore/blob/a24197d74648de19b3aa32d273e0fa84aad1bd6e/bookstore.jpg?raw=true) 

Image cropped from Ivo Rainha https://www.pexels.com/photo/top-view-of-library-with-red-stairs-1261180/.

### What's in this repository
- **Python program:** `shelf_track_dec25.py`  
- **Images:** visuals and reviewer feedback  

### Project Context

The task was to build a menu-driven program that allows a clerk to:

- Enter data about new books into the database  
- Update existing book information  
- Delete books from the system  
- Search for books based on availability

Beyond the core requirements, I extended the solution so that:

- **Author information is handled consistently**, recognising when an author already exists  
- Authors with multiple books are supported without duplication  
- Updates to author records propagate correctly across all relevant books

These extensions strengthened the logic of the system and made the experience more realistic.

### Approach and Key Features

This project combines **SQL database design** with **Python control flow** to build a usable inventory system:

- **SQLite database schema:** Designed to store books and related author data efficiently
- **SQL queries:** Structured DDL and DML statements to insert, update, delete, and read data
- **Python interface:** A text-based menu system drives user interaction and database operations
- **Sample data loading:** Optional loading from a correctly formatted file to populate the database

The program runs directly from the terminal with a user-friendly prompt for each action.

### Screenshot Gallery

Here are a few screenshots demonstrating the menu interface and sample outputs:

![Bookshelf menu screenshot](./book%20shelf%20menu.jpg)  
![Book details screenshot](./book%20shelf%20option%205%20book%20details.jpg)

### Reviewer Feedback

My [reviewer](./SQL%20feedback.jpg) noted that my solution was an **extensive and seamless interpretation of the brief**, with clear logic and thoughtful handling of the requirements. A gentle nudge on PEP8 style was also included — feedback which I’ve taken to heart and continue to apply across my projects.

### Skills Demonstrated

- Relational database design with SQL  
- SQL query construction (INSERT, UPDATE, DELETE, SELECT)  
- Python integration with SQLite  
- Menu-driven user interface design  
- Handling foreign key relationships and data consistency

### Requirements

This project uses Python 3 and the built-in `sqlite3` module. No additional Python packages are required.

### Why this project belongs in my portfolio

This project demonstrates practical SQL skills beyond single queries — it shows how a database supports a real-world workflow when paired with a controlling application. It also highlights my ability to think about data structure and logic holistically.
