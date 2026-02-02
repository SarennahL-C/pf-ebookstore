# Ebookstore — SQL Inventory and Menu-Driven Database Application

This project demonstrates the use of **SQL within a Python application** to manage an ebookstore’s inventory and operations. The solution integrates relational database design with Python control flow to support common business tasks such as adding, updating, querying, and deleting inventory records.

The project reflects both a disciplined approach to problem-solving and a strong appreciation for the **logical elegance of SQL**, particularly in how database design decisions shape query behaviour and system reliability.

![Ornate, multi-level bookstore with carved wooden railings, tall bookshelves filled with books, warm lighting from hanging lanterns, and a grand central staircase leading between floors. The tonal palette is warm and autumnal.](https://github.com/SarennahL-C/pf-ebookstore/blob/a24197d74648de19b3aa32d273e0fa84aad1bd6e/bookstore.jpg?raw=true)

<sub>Image cropped from Ivo Rainha, https://www.pexels.com/photo/top-view-of-library-with-red-stairs-1261180/</sub>

---

## What’s in this repository

- **Python program:** menu-driven inventory system (`shelf_track_dec25.py`)  
- **Images:** screenshots and reviewer feedback  

---

## Project Context

The task was to build a menu-driven application that allows a store clerk to manage an ebook inventory using a relational database. Core requirements included the ability to:

- Add new books to the database  
- Update existing book records  
- Delete books from the system  
- Search for books based on availability  

Beyond the core specification, the solution was extended to handle **author data consistently**, recognising shared authorship across multiple books and maintaining data integrity throughout the system.

---

## Approach Overview

This project combines **SQL database design** with **Python program structure** to create a practical, usable application:

- A **SQLite database schema** was designed to store books and related author information efficiently  
- SQL **DDL and DML queries** were used to insert, update, delete, and retrieve records  
- A **text-based menu interface** drives user interaction and database operations  
- Author records are reused where appropriate, avoiding duplication and ensuring consistency  
- Optional sample data loading supports easier testing and demonstration  

The application runs directly from the terminal and provides clear prompts for each available action.

---

## Key Features

- Robust handling of **author–book relationships**  
- Consistent updates across related records  
- Clear separation between user interface logic and database operations  
- Practical application of relational database principles  

---

## Screenshot Gallery

The screenshots below demonstrate the menu interface and example outputs:

![Bookshelf menu screenshot](./book%20shelf%20menu.jpg)  
![Book details screenshot](./book%20shelf%20option%205%20book%20details.jpg)

---

## Endorsement

Reviewer feedback described the solution as an **extensive and seamless interpretation of the brief**, highlighting:

- Clear and logical implementation of requirements  
- Thoughtful handling of relational data and author consistency  
- A robust, well-structured approach to integrating SQL with Python  

Minor feedback regarding **PEP8 style conventions** was also provided and has since been incorporated into subsequent projects.

<sub>[View full reviewer feedback](SQL%20feedback.jpg)</sub>

---

## Skills Demonstrated

**Databases**
- Relational database design  
- SQL query construction (INSERT, UPDATE, DELETE, SELECT)  
- Handling foreign key relationships  

**Programming**
- Python integration with SQLite  
- Menu-driven application design  
- Control flow and user input handling  

**Practice**
- Data consistency and integrity  
- Translating requirements into a working system  

---

## Requirements

This project uses **Python 3** and the built-in `sqlite3` module.  
No additional Python packages are required.

---

## Why this project belongs in my portfolio

This project demonstrates practical SQL skills beyond isolated queries, showing how relational databases support real-world workflows when paired with an application layer.

It highlights my ability to think holistically about data structure, system logic, and user interaction, and complements my notebook-based analytical work with a fully programmatic, production-style example.
